/**
 * FILENAME: main.js
 * GitGalaxy Phase 11: Direct JSON Visualization Core
 * Optimized for Spec v6.2 (Pre-analyzed JSONs)
 */

import { GalaxyEngine } from './core/galaxy-engine.js';
import { DataParser } from './core/data-parser.js';
import { createPhase6Shaders } from './core/phase-6-shaders.js';

class AppController {
    constructor() {
        this.engine = new GalaxyEngine();
        this.parser = new DataParser();
        
        this.searchIndex = [];
        this.discoveredGalaxies = []; 
        
        this.METRIC_NAMES = {
            1: "Cognitive Pressure",
            2: "Resilience Factor",
            3: "Structural Debt",
            4: "Verification Density",
            5: "Surface Exposure",
            11: "Seismic Churn"
        };

        this.init();
    }

    async init() {
        console.log("Visualizer: Initializing neural matrix...");
        
        try {
            // PHASE 11.1: Await Engine Readiness
            // We poll for the materials to ensure the WebGPU init is complete
            await this.waitForEngine();

            // Connect TSL Node Materials once engine is ready
            const shaders = createPhase6Shaders(this.engine);
            if (this.engine.solidMat && this.engine.wireMat) {
                this.engine.solidMat.colorNode = shaders.colorNode;
                this.engine.wireMat.colorNode = shaders.colorNode;
                this.engine.solidMat.opacityNode = shaders.opacityNode;
                this.engine.wireMat.opacityNode = shaders.opacityNode;
                
                // --- THE FIX: Force WebGPU to recompile the materials ---
                this.engine.solidMat.needsUpdate = true;
                this.engine.wireMat.needsUpdate = true;
            }

            window.isWebVisible = false;
            window.toggleDependencyWeb = function(btn) {
                window.isWebVisible = !window.isWebVisible;
                
                // Trigger the 3D Engine
                if (window.App && window.App.toggleLines) {
                    window.App.toggleLines(window.isWebVisible);
                }

                // Update Button Aesthetics
                if (window.isWebVisible) {
                    btn.innerText = "⎈ HIDE LOCAL WEB";
                    btn.style.background = "var(--accent)";
                    btn.style.color = "#000";
                    btn.style.boxShadow = "0 0 15px var(--accent)";
                } else {
                    btn.innerText = "⎈ VISUALIZE LOCAL WEB";
                    btn.style.background = "transparent";
                    btn.style.color = "var(--accent)";
                    btn.style.boxShadow = "none";
                }
            };

            window.App = {
                engine: this.engine,
                setTheme: (val) => this.handleThemeChange(val),
                setMetric: (val) => this.handleMetricChange(val),
                loadMock: (key) => this.fetchGalaxyData(key), 
                resetCamera: () => this.handleResetCamera(),
                hideHUDUI: () => window.hideHUDUI(),
                
                // --- NEW: Expose the toggle to the HTML ---
                toggleLines: (val) => {
                    const raw = window.currentRawGalaxyData;
                    const pScalar = raw?.meta?.scalars?.physics || 10;
                    this.engine.toggleDependencyLines(val, raw?.galaxy, pScalar);
                },

                toggleGlobalWeb: (val) => {
                    const raw = window.currentRawGalaxyData;
                    if (!raw || !raw.galaxy) return;
                    const pScalar = raw.meta?.scalars?.physics || 10;
                    this.engine.toggleGlobalWeb(val, raw.galaxy, pScalar);
                },
                syncSelection: () => this.syncHUDWithSelection()
            };

            // --- ADAPTIVE QUALITY LISTENER ---
            window.addEventListener('galaxy-quality-change', (e) => {
                const newTier = e.detail.tier;
                console.log(`Visualizer: Performance Shift -> ${newTier} Tier Active`);
                
                this.engine.currentQualityTier = newTier;

                // 1. CULL THE DUST FIELD: Hide it entirely if not on TITAN
                if (this.engine.dustField) {
                    this.engine.dustField.visible = (newTier === 'TITAN');
                }

                // 2. AUTO-CULL SATELLITES (Only on severe frame drops)
                const moonMesh = this.engine.meshGroups['moon'];
                if (moonMesh && newTier === 'POTATO') {
                    // Turn them off to save GPU fill-rate
                    moonMesh.visible = false;
                    
                    // Update the UI button so you know the system intervened
                    const btnSats = document.getElementById('btn-toggle-sats');
                    if (btnSats) {
                        btnSats.innerText = "Satellites: OFF (AUTO)";
                        btnSats.style.background = "transparent";
                    }
                }

                // 3. REBUILD THE WEB (If Active)
                if (window.isGlobalWebOn && window.currentRawGalaxyData) {
                    const raw = window.currentRawGalaxyData;
                    const pScalar = raw.meta?.scalars?.physics || 10;
                    
                    if (this.engine.globalWebMesh) {
                        this.engine.scene.remove(this.engine.globalWebMesh);
                        this.engine.globalWebMesh.children.forEach(c => { 
                            c.geometry.dispose(); 
                            c.material.dispose(); 
                        });
                        this.engine.globalWebMesh = null;
                    }
                    this.engine.toggleGlobalWeb(true, raw.galaxy, pScalar);
                }
            });

            // UI Event Listeners
            const searchInput = document.getElementById('warp-search');
            if (searchInput) {
                searchInput.addEventListener('input', (e) => this.performSearch(e.target.value));
            }

            // Auto-Discovery: Ask the Librarian what artifacts are available
            await this.discoverGalaxies();

            // Initial Teleport: Default to apollo-11 or apollo if available, else first found
            let defaultKey = this.discoveredGalaxies[0];
            if (this.discoveredGalaxies.includes('apollo-11')) deepKey = 'apollo-11';
            else if (this.discoveredGalaxies.includes('apollo')) defaultKey = 'apollo';
            
            if (defaultKey) {
                await this.fetchGalaxyData(defaultKey);
            } else {
                console.warn("Visualizer: No archives discovered in /backend.");
                // Hide loader anyway if no data found so user sees the empty UI
                this.clearLoader();
            }

        } catch (err) {
            console.error("Visualizer: Critical Initialization Error:", err);
            this.clearLoader();
        }
    }

    /**
     * Helper to wait for the async GalaxyEngine.init() to complete
     */
    async waitForEngine() {
        return new Promise((resolve, reject) => {
            let attempts = 0;
            const check = () => {
                attempts++;
                if (this.engine.solidMat) {
                    resolve();
                } else if (attempts > 200) { // 10 second timeout
                    reject("Engine failed to initialize materials within 10s. Check WebGPU support.");
                } else {
                    setTimeout(check, 50);
                }
            };
            check();
        });
    }

    /**
     * Force-clears the loading screen
     */
    clearLoader() {
        const loader = document.getElementById('loading-screen');
        if (loader) {
            loader.style.opacity = '0';
            setTimeout(() => loader.remove(), 1000);
        }
    }

    async discoverGalaxies() {
        try {
            const response = await fetch('/api/list_galaxies');
            if (response.ok) {
                this.discoveredGalaxies = await response.json();
                this.renderSystemMenu();
            }
        } catch (err) {
            console.error("Discovery Failed:", err);
        }
    }

    /**
     * DYNAMIC UI GENERATOR
     * Reads the JSON schema to populate the Spectral Analysis dropdown
     * and synchronizes the HUD text mapping.
     */
    buildMetricDropdown(riskNames) {
        const select = document.getElementById('metric-select');
        if (!select) return;

        const currentVal = select.value; 
        
        // 1. Reset everything to baseline
        select.innerHTML = '<option value="0">Standard (Basal State)</option>';
        this.METRIC_NAMES = {}; 

        window.RISK_SCHEMA = riskNames;

        // 2. Loop through the JSON schema and build the UI
        riskNames.forEach((rawName, index) => {
            // THE FIX: Try to grab the exact title from colors.js first!
            let cleanName = rawName.split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
            
            if (window.Colors && window.Colors.LEGENDS && window.Colors.LEGENDS[rawName]) {
                cleanName = window.Colors.LEGENDS[rawName].title;
            }
            
            const engineId = index + 1; 
            
            this.METRIC_NAMES[engineId] = cleanName;

            const option = document.createElement('option');
            option.value = engineId;
            option.innerText = cleanName;
            select.appendChild(option);
        });

        // --- NEW: 3. Inject Language Identity (Mode 14) ---
        const langModeId = 14;
        const langModeName = "Language Identity";
        this.METRIC_NAMES[langModeId] = langModeName;

        const langOption = document.createElement('option');
        langOption.value = langModeId;
        langOption.innerText = langModeName;
        select.appendChild(langOption);

        // 4. Restore previous selection
        if (this.METRIC_NAMES[currentVal]) {
            select.value = currentVal;
        } else {
            select.value = "0";
            this.handleMetricChange("0");
        }
    }

    renderSystemMenu() {
            const container = document.getElementById('galaxy-list'); 
            if (!container) return;
            container.innerHTML = ''; 

            this.discoveredGalaxies.forEach(key => {
                const btn = document.createElement('button');
                // USE THE OLD CYBER CSS CLASS INSTEAD OF TAILWIND
                btn.className = "warp-btn"; 
                
                // Replicate the old internal span style for the badge
                const cleanName = key.replace(/_/g, ' ').toUpperCase();
                btn.innerHTML = `${cleanName} <span>WARP</span>`;
                
                btn.onclick = () => this.fetchGalaxyData(key);
                container.appendChild(btn);
            });
        }

    /**
     * FETCH GALAXY DATA
     * Streams the pre-analyzed JSON directly into the 3D Parser.
     */
    async fetchGalaxyData(key) {
        console.log(`Visualizer: Fetching ${key}...`);

        const searchInput = document.getElementById('warp-search');
        if (searchInput) searchInput.value = '';
        if (window.renderSearchResults) window.renderSearchResults([], null);

        const progress = document.getElementById('load-progress');
        if (progress) {
            progress.style.transition = 'none';
            progress.style.width = '30%';
        }

        try {
            // 1. Fetch the data entirely in the background FIRST
            const response = await fetch(`/backend/${key}_galaxy.json`);
            if (!response.ok) throw new Error(`Artifact [${key}] Load Error: ${response.status}`);
            
            const raw = await response.json();

            // --- NEW: REVERSE-ENGINEER OUTBOUND EDGES ---
            // The JSON only ships with 'edges' (Imported By) to save space.
            // We flip them here to create 'outbound_edges' (Imports).
            if (raw.galaxy && raw.galaxy.edges && !raw.galaxy.outbound_edges) {
                raw.galaxy.outbound_edges = Array.from({length: raw.galaxy.names.length}, () => []);
                raw.galaxy.edges.forEach((importedByArray, targetId) => {
                    if (importedByArray) {
                        importedByArray.forEach(sourceId => {
                            raw.galaxy.outbound_edges[sourceId].push(targetId);
                        });
                    }
                });
            }

            window.currentRawGalaxyData = raw; 
            
            // --- NEW: INJECT STORY DATA INTO THE HTML HUD ---
            if (window.populateStoryHUD) {
                window.populateStoryHUD(raw.story, key);
            }
            
            if (raw.meta && raw.meta.schemas && raw.meta.schemas.risk_vector_x1000) {
                this.buildMetricDropdown(raw.meta.schemas.risk_vector_x1000);
            }

            if (progress) {
                progress.style.transition = 'width 0.5s ease';
                progress.style.width = '70%';
            }

            // 2. NOW trigger the visual warp, passing a callback for the exact midpoint!
            if (this.engine && typeof this.engine.hyperspaceJump === 'function') {
                this.engine.hyperspaceJump(() => {
                    // This code only runs when the camera is deep inside the black hole
                    this.engine.loadSector(raw);
                    this.buildSearchIndex(raw);
                    
                    if (progress) progress.style.width = '100%';
                    this.clearLoader();
                });
            } else {
                // Fallback if engine is missing the jump method
                this.engine.loadSector(raw);
                this.buildSearchIndex(raw);
                if (progress) progress.style.width = '100%';
                this.clearLoader();
            }

            const brand = document.getElementById('brand-title');
            if (brand) brand.innerText = key.split('-')[0].split('_')[0];

        } catch (err) {
            console.warn("Visualizer: Data load failed for", key, err);
            if (this.engine.loadMock) {
                this.engine.loadMock(key);
            }
            this.clearLoader();
        }
    }

    /**
     * SEARCH INDEXER
     * Maps the 'galaxy' object for the Warp Search.
     */
    buildSearchIndex(raw) {
        this.searchIndex = [];
        const gal = raw.galaxy;
        if (!gal || !gal.names) return;

        // --- THE FIX: Grab the physics scalar from the JSON meta ---
        const pScalar = raw.meta?.scalars?.physics || 10;

        for (let i = 0; i < gal.names.length; i++) {
            const star = {
                id: i,
                name: gal.names[i],
                type: 'FILE',
                loc: gal.locs[i],
                // --- THE FIX: Divide the raw integers to match the true 3D world ---
                pos: { 
                    x: gal.pos_x[i] / pScalar, 
                    y: gal.pos_y[i] / pScalar, 
                    z: gal.pos_z[i] / pScalar 
                }
            };
            this.searchIndex.push(star);

            if (gal.satellites && gal.satellites[i]) {
                gal.satellites[i].forEach(sat => {
                    this.searchIndex.push({
                        id: i,
                        name: sat[0], 
                        type: 'SATELLITE',
                        loc: sat[1],
                        pos: star.pos // Satellites correctly inherit the scaled parent position
                    });
                });
            }
        }
    }

    performSearch(query) {
        if (!query || query.length < 2) { window.renderSearchResults([], null); return; }
        const q = query.toLowerCase();
        const matches = this.searchIndex.filter(item => item.name.toLowerCase().includes(q)).slice(0, 8);
        window.renderSearchResults(matches, (selected) => {
            this.engine.flyTo(selected.pos, selected.id);
            this.syncHUDWithSelection();
        });
    }

    syncHUDWithSelection() {
        const sid = this.engine.uSelectedGlobalId.value;
        if (sid === -1) {
            this.engine.clearDependencyLines(); 
            return; 
        }
        
        const fileData = this.engine.activeFiles[sid];
        const raw = window.currentRawGalaxyData;
        
        let inEdges = [];
        let inNames = [];
        let outEdges = [];
        let outNames = [];

        if (raw && raw.galaxy) {
            // 1. Get Inbound (Imported By)
            if (raw.galaxy.edges) {
                inEdges = raw.galaxy.edges[sid] || [];
                inNames = inEdges.map(id => raw.galaxy.names[id]); 
            }
            // 2. Get Outbound (Imports)
            if (raw.galaxy.outbound_edges) {
                outEdges = raw.galaxy.outbound_edges[sid] || [];
                outNames = outEdges.map(id => raw.galaxy.names[id]);
            }
        }

        // Draw the 3D Lines
        const pScalar = raw?.meta?.scalars?.physics || 10;
        this.engine.drawDependencyLines(sid, inEdges, outEdges, raw.galaxy, pScalar);

        // Pass BOTH arrays to the HTML HUD
        if (fileData && window.updateHUD) {
            const mode = this.engine.uMetricMode.value;
            window.updateHUD(fileData, mode, this.METRIC_NAMES[mode], inNames, inEdges.length, outNames, outEdges.length);
        }
    }

    handleThemeChange(val) { 
        const index = parseInt(val);
        this.engine.uThemeIndex.value = index; 

        // 1. Handle Background Environments
        if (index === 4) { // High-Vis
            this.engine.scene.background.setHex(0xffffff); // Pure White
        } else if (index === 3) { // Matrix
            this.engine.scene.background.setHex(0x000000); // Pure Black
        } else if (index === 1) { // Ice Crystal
            this.engine.scene.background.setHex(0x020205); // Dark Navy
        } else { // Galactic / Basal
            this.engine.scene.background.setHex(0x050508); // Deep Grey-Black
        }

        // 2. Handle Wireframe Overrides
        const forceWireframe = (index === 3);
        this.engine.solidMat.wireframe = forceWireframe;
        this.engine.solidMat.needsUpdate = true;
        
        // 3. Handle DOM Label Colors
        const labelContainer = document.getElementById('label-container');
        if (labelContainer) {
            // Strip any existing theme classes
            labelContainer.className = ''; 
            
            // Apply the new theme class
            if (index === 2) labelContainer.classList.add('theme-galactic');
            else if (index === 3) labelContainer.classList.add('theme-matrix');
            else if (index === 4) labelContainer.classList.add('theme-high-vis');
            // (Ice Crystal uses the default CSS, so it needs no class)
        }

        // --- NEW: Force the Legend & HUD to refresh their colors ---
        this.handleMetricChange(this.engine.uMetricMode.value);
    }

    handleMetricChange(val) { 
        const mode = parseInt(val);
        this.engine.uMetricMode.value = mode; 
        
        // Broadcast the legend update globally
        if (window.updateLegend) {
            let schemaKey = null;
            if (mode === 14) {
                schemaKey = 'language_identity'; // Pass a custom flag for Mode 14
            } else if (mode > 0) {
                schemaKey = window.RISK_SCHEMA[mode - 1]; // Normal 0-indexed schema lookup
            }
            window.updateLegend(mode, schemaKey);
        }

        this.syncHUDWithSelection(); 
    }


    handleResetCamera() {
        this.engine.hideHUD();
        new TWEEN.Tween(this.engine.targetPos).to({ x: 0, y: 0, z: 0 }, 1500).easing(TWEEN.Easing.Cubic.Out).start();
        new TWEEN.Tween(this.engine).to({ cameraRadius: 5000 }, 1500).easing(TWEEN.Easing.Cubic.Out).start();
    }

    

}



new AppController();