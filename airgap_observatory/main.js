/**
 * GitGalaxy
 * Copyright (c) 2026 Joe Esquibel
 *
 * This source code is licensed under the PolyForm Noncommercial License 1.0.0.
 * You may not use this file except in compliance with the License.
 * A copy of the license can be found in the LICENSE file in the root directory
 * of this project, or at https://polyformproject.org/licenses/noncommercial/1.0.0/
 */
/**
 * FILENAME: main.js
 * GitGalaxy Phase 11: Direct JSON Visualization Core
 * Optimized for Spec v6.2 (Pre-analyzed JSONs) & Airgap Environments
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
            await this.waitForEngine();

            // Connect TSL Node Materials once engine is ready
            const shaders = createPhase6Shaders(this.engine);
            if (this.engine.solidMat && this.engine.wireMat) {
                this.engine.solidMat.colorNode = shaders.colorNode;
                this.engine.wireMat.colorNode = shaders.colorNode;
                this.engine.solidMat.opacityNode = shaders.opacityNode;
                this.engine.wireMat.opacityNode = shaders.opacityNode;
                
                // Force WebGPU to recompile the materials
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

            // --- THE AIRGAP DRAG-AND-DROP LISTENER (With RAM Caching & Safety Limits) ---
            window.addEventListener('dragover', (e) => { e.preventDefault(); });
            window.addEventListener('drop', (e) => {
                e.preventDefault();
                const file = e.dataTransfer.files[0];
                
                if (file && file.name.endsWith('.json')) {
                    // 1. Safety Failsafe: 50MB Limit
                    const maxSize = 50 * 1024 * 1024; 
                    if (file.size > maxSize) {
                        alert(`File is too large (${(file.size / 1024 / 1024).toFixed(1)}MB).\n\nTo prevent browser memory crashes, please move files larger than 50MB directly into your local ./data/ folder and refresh the page to auto-discover them.`);
                        return;
                    }

                    const loader = document.getElementById('loading-screen');
                    if (loader) { loader.style.opacity = '1'; loader.style.display = 'flex'; }
                    
                    const reader = new FileReader();
                    reader.onload = (event) => {
                        try {
                            const raw = JSON.parse(event.target.result);
                            
                            // 2. RAM Caching Logic: Add to the sidebar menu
                            const baseName = file.name.replace('_galaxy.json', '').replace('.json', '');
                            const exists = this.discoveredGalaxies.find(g => g.id === baseName);

                            if (!exists) {
                                this.discoveredGalaxies.push({
                                    id: baseName,
                                    name: baseName.replace(/-/g, ' ').toUpperCase(),
                                    file: file.name,
                                    isRAM: true, // Special flag to bypass network fetch
                                    rawData: raw // Cache the parsed JSON object directly in RAM
                                });
                                this.renderSystemMenu(); // Re-draw the buttons
                            }

                            this.loadGalaxyFromRAM(raw, file.name);
                        } catch (err) {
                            console.error("Airgap Parse Failure:", err);
                            this.clearLoader();
                            alert("Critical Error: Failed to parse JSON file. The file may be corrupted.");
                        }
                    };
                    reader.readAsText(file);
                }
            });

            // UI Event Listeners
            const searchInput = document.getElementById('warp-search');
            if (searchInput) {
                searchInput.addEventListener('input', (e) => this.performSearch(e.target.value));
            }

            // --- AUTO-DISCOVER LOCAL DATA ---
            await this.discoverGalaxies();

            // --- THE AIRGAP DRAG-AND-DROP LISTENER ---
            window.addEventListener('dragover', (e) => { e.preventDefault(); });
            window.addEventListener('drop', (e) => {
                e.preventDefault();
                const file = e.dataTransfer.files[0];
                if (file && file.name.endsWith('.json')) {
                    const loader = document.getElementById('loading-screen');
                    if (loader) { loader.style.opacity = '1'; loader.style.display = 'flex'; }
                    
                    const reader = new FileReader();
                    reader.onload = (event) => {
                        try {
                            const raw = JSON.parse(event.target.result);
                            this.loadGalaxyFromRAM(raw, file.name);
                        } catch (err) {
                            console.error("Airgap Parse Failure:", err);
                            this.clearLoader();
                        }
                    };
                    reader.readAsText(file);
                }
            });

            // Start in an empty state waiting for data or a file drop
            this.clearLoader();
            const brand = document.getElementById('brand-title');
            if (brand) brand.innerText = "AWAITING TELEMETRY...";

        } catch (err) {
            console.error("Visualizer: Critical Initialization Error:", err);
            this.clearLoader();
        }
    }

    async waitForEngine() {
        return new Promise((resolve, reject) => {
            let attempts = 0;
            const check = () => {
                attempts++;
                if (this.engine.solidMat) {
                    resolve();
                } else if (attempts > 200) { 
                    reject("Engine failed to initialize materials within 10s. Check WebGPU support.");
                } else {
                    setTimeout(check, 50);
                }
            };
            check();
        });
    }

    clearLoader() {
        const loader = document.getElementById('loading-screen');
        if (loader) {
            loader.style.opacity = '0';
            setTimeout(() => loader.remove(), 1000);
        }
    }

    async discoverGalaxies() {
        try {
            // Fetch the directory itself
            const response = await fetch('./data/');
            if (!response.ok) throw new Error("Could not read data directory");
            
            const htmlText = await response.text();
            
            // Create a temporary DOM to parse Python's HTML links
            const parser = new DOMParser();
            const doc = parser.parseFromString(htmlText, 'text/html');
            const links = Array.from(doc.querySelectorAll('a'));
            
            this.discoveredGalaxies = [];
            
            // Hunt for galaxy files and guess their accompanying audit/llm files
            links.forEach(link => {
                const filename = link.getAttribute('href');
                if (filename && filename.endsWith('_galaxy.json')) {
                    const baseName = filename.replace('_galaxy.json', '');
                    
                    this.discoveredGalaxies.push({
                        id: baseName,
                        name: baseName.replace(/-/g, ' ').toUpperCase(),
                        file: filename,
                        auditUrl: `./data/${baseName}_galaxy_audit.json`,
                        llmUrl: `./data/${baseName}_galaxy_llm.md`
                    });
                }
            });

            if (this.discoveredGalaxies.length > 0) {
                this.renderSystemMenu();
                await this.fetchGalaxyData(this.discoveredGalaxies[0]);
            } else {
                console.warn("No _galaxy.json files found in ./data/. Waiting for Drag-and-Drop.");
                this.clearLoader();
            }
        } catch (err) {
            console.error("Directory Scan Failed. Operating in Drag-and-Drop mode only.", err);
            this.clearLoader();
        }
    }

    buildMetricDropdown(riskNames) {
        const select = document.getElementById('metric-select');
        if (!select) return;

        const currentVal = select.value; 
        select.innerHTML = '<option value="0">Standard (Basal State)</option>';
        this.METRIC_NAMES = {}; 
        window.RISK_SCHEMA = riskNames;

        riskNames.forEach((rawName, index) => {
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

        const langModeId = 14;
        const langModeName = "Language Identity";
        this.METRIC_NAMES[langModeId] = langModeName;
        const langOption = document.createElement('option');
        langOption.value = langModeId;
        langOption.innerText = langModeName;
        select.appendChild(langOption);

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

        this.discoveredGalaxies.forEach(galaxyObj => {
            const btn = document.createElement('button');
            btn.className = "warp-btn"; 
            btn.innerHTML = `${galaxyObj.name} <span>WARP</span>`;
            btn.onclick = () => this.fetchGalaxyData(galaxyObj);
            container.appendChild(btn);
        });
    }

    async fetchGalaxyData(galaxyObj) {
        if (typeof galaxyObj === 'string') {
            galaxyObj = { id: galaxyObj, name: galaxyObj };
        }
        
        const key = galaxyObj.id;
        
        const progress = document.getElementById('load-progress');
        if (progress) {
            progress.style.transition = 'none';
            progress.style.width = '30%';
        }

        try {
            // --- NEW: Bypass Network for Drag-and-Drop Files ---
            if (galaxyObj.isRAM) {
                console.log(`Visualizer: Restoring [${key}] directly from RAM Cache...`);
                
                // Set injected URLs to null so the payload buttons correctly show "MISSING"
                galaxyObj.rawData._injectedAuditUrl = null;
                galaxyObj.rawData._injectedLlmUrl = null;
                
                this.loadGalaxyFromRAM(galaxyObj.rawData, galaxyObj.file);
                
                const brand = document.getElementById('brand-title');
                if (brand) brand.innerText = galaxyObj.name;
                return; // Exit early!
            }

            // --- NORMAL: Local Directory Fetch ---
            console.log(`Visualizer: Fetching [${key}] from local ./data/ folder...`);
            const localPath = `./data/${galaxyObj.file}`;
            const response = await fetch(localPath);
            if (!response.ok) throw new Error(`Artifact [${key}] Load Error: ${response.status}`);
            
            const raw = await response.json();

            raw._injectedAuditUrl = galaxyObj.auditUrl;
            raw._injectedLlmUrl = galaxyObj.llmUrl;

            this.loadGalaxyFromRAM(raw, galaxyObj.file);
            
            const brand = document.getElementById('brand-title');
            if (brand) brand.innerText = galaxyObj.name;

        } catch (err) {
            console.warn("Visualizer: Local data load failed for", key, err);
            this.clearLoader();
            alert(`Failed to load ${key}. Please check the console for details.`);
        }
    }

    loadGalaxyFromRAM(raw, filename) {
        console.log(`Visualizer: Loading ${filename} from local memory...`);

        const progress = document.getElementById('load-progress');
        if (progress) {
            progress.style.transition = 'width 0.5s ease';
            progress.style.width = '70%';
        }

        try {
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
            
            if (window.populateStoryHUD) {
                window.populateStoryHUD(raw.story, filename);
            }

            if (window.checkAndBindPayloads) {
                window.checkAndBindPayloads(filename);
            }
            
            if (raw.meta && raw.meta.schemas && raw.meta.schemas.risk_vector_x1000) {
                this.buildMetricDropdown(raw.meta.schemas.risk_vector_x1000);
            }

            if (this.engine && typeof this.engine.hyperspaceJump === 'function') {
                this.engine.hyperspaceJump(() => {
                    this.engine.loadSector(raw);
                    this.buildSearchIndex(raw);
                    if (progress) progress.style.width = '100%';
                    this.clearLoader();
                });
            } else {
                this.engine.loadSector(raw);
                this.buildSearchIndex(raw);
                if (progress) progress.style.width = '100%';
                this.clearLoader();
            }

            const brand = document.getElementById('brand-title');
            if (brand) brand.innerText = filename.replace('_galaxy.json', '').toUpperCase();

        } catch (err) {
            console.warn("Visualizer: RAM load failed", err);
            this.clearLoader();
        }
    }

    buildSearchIndex(raw) {
        this.searchIndex = [];
        const gal = raw.galaxy;
        if (!gal || !gal.names) return;

        const pScalar = raw.meta?.scalars?.physics || 10;

        for (let i = 0; i < gal.names.length; i++) {
            const star = {
                id: i,
                name: gal.names[i],
                type: 'FILE',
                loc: gal.locs[i],
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
                        pos: star.pos 
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
            if (raw.galaxy.edges) {
                inEdges = raw.galaxy.edges[sid] || [];
                inNames = inEdges.map(id => raw.galaxy.names[id]); 
            }
            if (raw.galaxy.outbound_edges) {
                outEdges = raw.galaxy.outbound_edges[sid] || [];
                outNames = outEdges.map(id => raw.galaxy.names[id]);
            }
        }

        const pScalar = raw?.meta?.scalars?.physics || 10;
        this.engine.drawDependencyLines(sid, inEdges, outEdges, raw.galaxy, pScalar);

        if (fileData && window.updateHUD) {
            const mode = this.engine.uMetricMode.value;
            window.updateHUD(fileData, mode, this.METRIC_NAMES[mode], inNames, inEdges.length, outNames, outEdges.length);
        }
    }

    handleThemeChange(val) { 
        const index = parseInt(val);
        this.engine.uThemeIndex.value = index; 

        if (index === 4) { 
            this.engine.scene.background.setHex(0xffffff); 
        } else if (index === 3) { 
            this.engine.scene.background.setHex(0x000000); 
        } else if (index === 1) { 
            this.engine.scene.background.setHex(0x020205); 
        } else { 
            this.engine.scene.background.setHex(0x050508); 
        }

        const forceWireframe = (index === 3);
        this.engine.solidMat.wireframe = forceWireframe;
        this.engine.solidMat.needsUpdate = true;
        
        const labelContainer = document.getElementById('label-container');
        if (labelContainer) {
            labelContainer.className = ''; 
            if (index === 2) labelContainer.classList.add('theme-galactic');
            else if (index === 3) labelContainer.classList.add('theme-matrix');
            else if (index === 4) labelContainer.classList.add('theme-high-vis');
        }

        this.handleMetricChange(this.engine.uMetricMode.value);
    }

    handleMetricChange(val) { 
        const mode = parseInt(val);
        this.engine.uMetricMode.value = mode; 
        
        if (window.updateLegend) {
            let schemaKey = null;
            if (mode === 14) {
                schemaKey = 'language_identity'; 
            } else if (mode > 0) {
                schemaKey = window.RISK_SCHEMA[mode - 1]; 
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