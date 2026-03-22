/**
 * VISUAL MATERIAL SYSTEM
 * Location: js/visual/materials.js
 * Responsibility: Manages the "Look" of the universe (Themes, Metrics, Colors).
 * Dependencies: js/config/colors.js
 */

class MaterialCache {
    constructor() {
        this.cache = {};
        this.activeThemeKey = 'ice-crystal';
        this.activeMetric = 'none';
    }

    /**
     * Internal helper to resolve color based on theme rules.
     * Handles basal colors, variance arrays (Galactic), and fallback logic.
     */
    resolveBasalColor(seedString = "") {
        const palette = window.Colors || { BEHAVIOR: { standard: 0xcccccc } };
        const themeCfg = palette.THEMES?.[this.activeThemeKey];
        
        // Check for variance/palette array in the active theme
        const colorArray = themeCfg ? (themeCfg.basalVariance || themeCfg.basalPalette) : null;

        if (colorArray && colorArray.length > 0) {
            // Deterministic hash to pick a consistent color for this file based on its name
            let hash = 0;
            for (let i = 0; i < seedString.length; i++) hash = seedString.charCodeAt(i) + ((hash << 5) - hash);
            const index = Math.abs(hash) % colorArray.length;
            return colorArray[index];
        }
        
        // Fallback to single basal color if variance array doesn't exist
        return themeCfg ? themeCfg.basalColor : 0xffffff;
    }

    /**
     * THE LOGIC GATE (Data Focus Protocol)
     * Determines the physical properties of the material based on the current mode.
     * - Metric 'none': Returns aesthetic basal color.
     * - Metric active: Applies dimming (Ghost Mode) or Highlighting (Signal Mode).
     */
    resolveMaterialProperties(tint, metrics, seedString, metricMode) {
        let hex;
        let opacity = (tint === 'scaffolding') ? 0.4 : 0.9;
        let emissiveIntensity = 1.5;
        let isDimmed = false;

        // 1. Basal State (No Metric Active)
        if (metricMode === 'none') {
            hex = this.resolveBasalColor(seedString);
        } 
        // 2. Active Analysis State
        else {
            const score = metrics[metricMode] || 0;
            let isRelevant = false;

            // Threshold Logic per Metric Type
            if (metricMode === 'safety') isRelevant = score > 50; // Safety highlights HIGH scores
            else isRelevant = score > 0; // Debt/Churn highlights ANY non-zero score

            if (isRelevant) {
                // High Signal: Use the Metric Color (Red, Cyan, Orange, etc.)
                hex = window.Colors.getMetricColor(metricMode, score);
                emissiveIntensity = 2.5; // Boost glow for data hotspots
                opacity = 1.0;
            } else {
                // Low Signal: Apply Data Focus Protocol (Dimming)
                hex = this.resolveBasalColor(seedString);
                
                const theme = window.Colors.THEMES[this.activeThemeKey];
                // Fetch dimming factor from theme (Galactic = 0.2, Ice = 1.0)
                const dimFactor = theme ? theme.dimmingFactor : 0.2;
                
                // If dimFactor < 1.0, we apply the "Ghost Mode" effect
                if (dimFactor < 1.0) {
                    opacity = 0.1; 
                    emissiveIntensity = 0.0; // Kill glow
                    isDimmed = true;
                }
            }
        }

        return { hex, opacity, emissiveIntensity, isDimmed };
    }

    /**
     * Get or Create Material
     * Returns a Three.js MeshStandardMaterial based on the requested parameters.
     * Caches the result to prevent memory leaks during render loops.
     */
    get(texture, tint, metrics, seedString) {
        // Cache key includes the current metric state to ensure we don't reuse
        // a "dimmed" material when the user switches modes.
        const currentMetricVal = metrics[this.activeMetric] || 0;
        const key = `${texture}_${tint}_${seedString}_${this.activeMetric}_${currentMetricVal}`;
        
        if (this.cache[key]) return this.cache[key];

        const props = this.resolveMaterialProperties(tint, metrics, seedString, this.activeMetric);

        const mat = new THREE.MeshStandardMaterial({
            color: props.hex,
            emissive: props.hex,
            emissiveIntensity: props.emissiveIntensity,
            roughness: (texture === 'crystalline') ? 0.0 : 0.2,
            metalness: 0.8,
            flatShading: true,
            transparent: true,
            opacity: props.opacity,
            wireframe: (texture === 'scaffolding')
        });

        // Store metadata for refreshing later without rebuilding geometry
        mat.userData = { texture, tint, metrics, seedString };
        this.cache[key] = mat;
        return mat;
    }

    /**
     * Refreshes all materials in the cache in-place.
     * Called when the user changes Theme or toggles a Metric.
     */
    refresh(newThemeKey, newMetricMode) {
        this.activeThemeKey = newThemeKey;
        if (newMetricMode) this.activeMetric = newMetricMode;

        for (let key in this.cache) {
            const mat = this.cache[key];
            const { texture, tint, metrics, seedString } = mat.userData;

            // Recalculate properties based on new state
            const props = this.resolveMaterialProperties(tint, metrics, seedString, this.activeMetric);

            mat.color.setHex(props.hex);
            mat.emissive.setHex(props.hex);
            mat.emissiveIntensity = props.emissiveIntensity;
            mat.opacity = props.opacity;
            
            // Special handling for High Vis / Matrix overrides
            if (newThemeKey === 'matrix') mat.emissiveIntensity = 2.5;
            else if (newThemeKey === 'high-vis') mat.emissiveIntensity = 0.0;
        }
    }
}

// Global Export
window.MaterialCache = MaterialCache;