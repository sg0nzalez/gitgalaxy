/**
 * THE GALAXYSCOPE (Telemetry & Adaptive Quality Sensor)
 * v2.3 - Ergonomic Relocation Edition (Phase 3 Integration)
 * Location: js/tools/perf_monitor.js
 * Trigger: Tilde Key (~)
 * * * FEATURES:
 * - RELOCATED: Now anchored to the bottom-left gutter (right of the main panel).
 * - Thematic Decoupling: Utilizes CSS variables and the Colors.js registry.
 * - Inversion Logic: Automatically switches to high-contrast mode for light themes.
 * - Real-time FPS Tracking (Rolling 3-second window)
 * - Memory Utilization (Chrome/Edge Engine)
 * - Island Count monitoring for the Spatial Island Registry.
 * - Adaptive Quality Emission: Dispatches 'galaxy-quality-change' for tiers.
 * - Hysteresis Logic: Prevents tier-flickering during minor FPS dips.
 */

class GalaxyScope {
    constructor() {
        this.active = false;
        this.domElement = null;
        
        // Monitoring Stats
        this.lastTime = performance.now();
        this.frameCount = 0;
        this.fps = 60;
        this.fpsHistory = []; // Rolling window for stability
        this.historySize = 3; // 3-second average
        
        // Quality State Management
        this.currentTier = 'TITAN'; // Default assumption
        this.tierStabilityCounter = 0; // Hysteresis buffer
        this.hysteresisThreshold = 5; // Seconds to confirm a tier change
        
        this.init();
    }

    /**
     * Initializes the telemetry interface and key listeners
     */
    init() {
        // 1. Create DOM (Hidden by default)
        this.createDOM();

        // 2. Tilde Key Listener for HUD toggling
        window.addEventListener('keydown', (e) => {
            if (e.key === '`' || e.key === '~') {
                e.preventDefault();
                this.toggle();
            }
        });

        console.log("🔭 GalaxyScope: Relocated to Bottom-Left Gutter (Press '~')");
    }

    /**
     * Constructs the high-fidelity diagnostic HUD
     * v2.3 UPDATE: Positioning changed to Bottom-Left for cleaner viewport.
     */
    createDOM() {
        this.domElement = document.createElement('div');
        Object.assign(this.domElement.style, {
            position: 'fixed',
            // PHASE 3 RELOCATION:
            bottom: '25px', // Anchor to bottom
            left: '340px',   // Offset right of the 320px sidebar + 20px padding
            top: 'unset',    // Clear top
            right: 'unset',  // Clear right
            
            width: '220px',
            backgroundColor: 'var(--bg-ui)',
            border: '1px solid var(--accent)',
            color: 'var(--accent)',
            fontFamily: '"Space Mono", monospace',
            fontSize: '10px',
            padding: '15px',
            display: 'none',
            zIndex: '10000',
            pointerEvents: 'none',
            boxShadow: '0 10px 30px rgba(0, 0, 0, 0.8)',
            borderRadius: '4px',
            lineHeight: '1.6',
            transition: 'all 0.3s ease' // Smooth transition for theme swaps
        });

        this.domElement.innerHTML = `
            <div style="border-bottom: 1px solid #334; margin-bottom: 8px; font-weight:bold; display:flex; justify-content:space-between; letter-spacing: 1px;">
                <span>GALAXY_SCOPE</span>
                <span id="gs-ver">v5.4.1</span>
            </div>
            <div style="display:grid; grid-template-columns: 1fr 1fr; gap: 5px; margin-bottom: 8px;">
                <div>FPS: <b id="gs-fps" style="color:inherit">--</b></div>
                <div style="text-align:right">MEM: <b id="gs-mem" style="color:inherit">--</b></div>
            </div>
            <div style="margin-top:5px; border-top: 1px dashed #334; padding-top:8px;">
                <div style="margin-bottom: 4px;">TIER: <b id="gs-tier" style="color:inherit; text-transform: uppercase;">TITAN</b></div>
                <div style="opacity: 0.8;">NODES: <b id="gs-ent">--</b></div>
                <div style="opacity: 0.8;">ISLANDS: <b id="gs-isl">--</b></div>
                <div style="opacity: 0.8;">DRAWS: <b id="gs-draw">--</b></div>
                <div style="opacity: 0.8;">TRIS:  <b id="gs-tris">--</b></div>
            </div>
            <div id="gs-footer" style="font-size: 13px; margin-top: 10px; opacity: 0.5; text-align: center;">
                CELESTIAL ISLAND ARCHITECTURE ACTIVE
            </div>
        `;

        document.body.appendChild(this.domElement);
    }

    /**
     * PHASE 2: Theme Synchronization
     * Updates the HUD visuals to match the global theme registry.
     * @param {string} key - Theme key (e.g., 'high-vis', 'matrix')
     */
    setTheme(key) {
        if (!window.Colors || !window.Colors.THEMES[key] || !this.domElement) return;
        
        const theme = window.Colors.THEMES[key];
        
        // 1. Update Core Container Styles
        this.domElement.style.backgroundColor = theme.uiPanel || 'rgba(5, 5, 8, 0.95)';
        this.domElement.style.borderColor = theme.uiAccent || '#00f3ff';
        this.domElement.style.color = theme.uiText || '#00f3ff';

        // 2. High-Vis Polish: If background is white, ensure shadows don't make it look "dirty"
        if (key === 'high-vis') {
            this.domElement.style.boxShadow = '0 5px 15px rgba(0,0,0,0.1)';
            this.domElement.style.borderWidth = '2px';
        } else {
            this.domElement.style.boxShadow = '0 10px 30px rgba(0, 0, 0, 0.8)';
            this.domElement.style.borderWidth = '1px';
        }
    }

    /**
     * Toggles the visibility of the performance HUD
     */
    toggle() {
        this.active = !this.active;
        this.domElement.style.display = this.active ? 'block' : 'none';
        
        // Sync on open to ensure colors match current state
        if (this.active && window.App && window.App.currentThemeKey) {
            this.setTheme(window.App.currentThemeKey);
        }
    }

    /**
     * Main telemetry loop - called from the 3D Engine's animation cycle
     */
    update(renderer) {
        // 1. Calculate Instant FPS
        this.frameCount++;
        const now = performance.now();
        if (now - this.lastTime >= 1000) {
            const instantFps = this.frameCount;
            this.frameCount = 0;
            this.lastTime = now;

            // 2. Rolling Average (Smoothing jitter)
            this.fpsHistory.push(instantFps);
            if (this.fpsHistory.length > this.historySize) this.fpsHistory.shift();
            
            const avgFps = this.fpsHistory.reduce((a, b) => a + b, 0) / this.fpsHistory.length;
            this.fps = Math.round(avgFps);

            // 3. Assess Quality Tier based on stable average
            this.assessQuality(this.fps);

            // 4. Update UI if active
            if (this.active) this.renderStats(renderer);
        }
    }

    /**
     * Performance-Aware Tier Assessment
     * Adjusts the simulation fidelity to maintain cinematic fluidiy
     */
    assessQuality(avgFps) {
        let detectedTier = this.currentTier;

        // Adaptive Thresholds
        if (avgFps >= 55) detectedTier = 'TITAN';
        else if (avgFps >= 35) detectedTier = 'STANDARD';
        else detectedTier = 'POTATO';

        // Hysteresis Check: Ensures performance dips are persistent before shifting
        if (detectedTier !== this.currentTier) {
            this.tierStabilityCounter++;
            if (this.tierStabilityCounter >= this.hysteresisThreshold) {
                this.changeTier(detectedTier);
                this.tierStabilityCounter = 0;
            }
        } else {
            this.tierStabilityCounter = 0; // Reset if the tier remains stable
        }
    }

    /**
     * Signals the entire system to scale visuals
     */
    changeTier(newTier) {
        console.warn(`GalaxyScope: Performance Shift Detected. Transitioning to [${newTier}] Tier.`);
        this.currentTier = newTier;
        
        // Dispatch Global Event for Engine3D to catch
        window.dispatchEvent(new CustomEvent('galaxy-quality-change', { 
            detail: { tier: newTier } 
        }));

        // Flash HUD indicator if visible
        if (this.active) {
            const elTier = document.getElementById('gs-tier');
            // Use current text color for restoration, fallback to theme accent if needed
            const originalColor = elTier.style.color; 
            elTier.style.color = '#ff0033'; // Warning Red
            setTimeout(() => elTier.style.color = originalColor || 'inherit', 500);
        }
    }

    /**
     * Injects real-time metrics into the DOM
     */
    renderStats(renderer) {
        if (!renderer || !renderer.info) return;

        // 1. Memory Metric (Chrome/Edge Only)
        let mem = "N/A";
        if (performance.memory) {
            mem = Math.round(performance.memory.usedJSHeapSize / 1048576) + " MB";
        }

        // 2. Scene Registry Intelligence
        let nodeCount = 0;
        if (window.App && window.App.engine) {
            // Count the total instances rendered across all star types
            const meshes = window.App.engine.meshGroups;
            if (meshes) {
                Object.values(meshes).forEach(m => nodeCount += m.count);
            }
        }

        // 3. WebGL Draw Telemetry
        const draws = renderer.info.render.calls;
        const tris = renderer.info.render.triangles;

        // 4. Update DOM Elements
        document.getElementById('gs-fps').innerText = this.fps;
        document.getElementById('gs-mem').innerText = mem;
        document.getElementById('gs-tier').innerText = this.currentTier;
        document.getElementById('gs-ent').innerText = nodeCount;
        document.getElementById('gs-isl').innerText = islandCount; // Phase 3 Metric
        document.getElementById('gs-draw').innerText = draws;
        document.getElementById('gs-tris').innerText = (tris / 1000).toFixed(1) + "k";

        // 5. Visual Stress Colors
        const elFps = document.getElementById('gs-fps');
        if (this.fps < 30) elFps.style.color = '#ff0033'; // Emergency Red
        else if (this.fps < 50) elFps.style.color = '#ffaa00'; // Caution Amber
        else elFps.style.color = 'inherit'; // Optimal (Theme Inherited)
    }
}

// Auto-Instantiate singleton
window.GalaxyScope = new GalaxyScope();