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
 * COLORS & PALETTE REGISTRY v5.4
 * Defines the "Visual Semantics" of the universe.
 * * INTEGRATED: Full 15-Metric Logic + HUD Legends
 * * UPDATED v5.4: Added String-based UI Metadata for perf_monitor (GalaxyScope) sync.
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
 * This file acts as the single source of truth for both the 3D WebGL Engine 
 * (using numeric hex) and the DOM-based UI layer (using CSS strings).
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
 */

const Colors = {
    // 1. BEHAVIORAL PALETTE (Metric Overlays)
    // These colors "bleed" through or override the basal state when toggled.
    BEHAVIOR: {
        standard: 0xcccccc,
        white: 0xffffff,
        
        // --- 1. The Red/Orange/Yellow Spectrum ---
        safety_crimson: 0xcc0000,    // Safety (Max)
        churn_orange: 0xff6d00,      // Churn (Max)
        flux_lime: 0xbfff00,         // State Flux (Max)
        docs_gold: 0xffd700,         // Docs (Min - Encyclopedic)
        docs_umber: 0x8da3bd,        // Docs (Max - Undocumented)
        spaces_yellow: 0xffff00,     // Civil War
        
        // --- 2. The Green/Teal/Cyan Spectrum ---
        stability_green: 0x76ff03,   // Stability (Min - Hot/New)
        tabs_green: 0x39ff14,        // Civil War
        verification_teal: 0x00b3b3, // Verification (Max)
        shield_cyan: 0x00f3ff,       // Safety (Min) & Ownership
        
        // --- 3. The Blue/Indigo/Violet Spectrum ---
        debt_blue: 0x0044cc,         // Tech Debt (Max)
        spec_blue: 0x0077ff,         // Spec Match (Max)
        mixed_blue: 0x0000ff,        // Civil War
        graveyard_slate: 0x483d8b,   // Graveyard (Max)
        concurrency_uv: 0xff4500,    // Concurrency (Max)
        
        // --- 4. The Purple/Pink/Rose Spectrum ---
        cognitive_purple: 0xcc00ff,  // Cognitive Load (Max)
        coverage_pink: 0xff00ff,     // Ownership (Max)
        api_rose: 0xff007f,          // API Exposure (Max)
        
    },

    // 5. LANGUAGE IDENTITY PALETTE (Spec 2.2.R)
    LANGUAGES: {
        'javascript': 0xF1E05A, 'js': 0xF1E05A,
        'typescript': 0x0099FF, 'ts': 0x0099FF,
        'python': 0x5C95FF, 'py': 0x5C95FF,
        'java': 0xE69F50,
        'c': 0xA8B9CC,
        'c++': 0xFF2E8C, 'cpp': 0xFF2E8C,
        'rust': 0xFF7B00, 'rs': 0xFF7B00,
        'go': 0x00E0FF,
        'c#': 0x49E33B, 'cs': 0x49E33B,
        'php': 0x9B86FF,
        'ruby': 0xFF4040, 'rb': 0xFF4040,
        'swift': 0xFF6A00,
        'kotlin': 0xC792EA, 'kt': 0xC792EA,
        'objective-c': 0x4DA6FF, 'm': 0x4DA6FF,
        'shell': 0x00FF00, 'bash': 0x00FF00, 'sh': 0x00FF00,
        'perl': 0x00C4FF, 'pl': 0x00C4FF,
        'lua': 0x5E80FF,
        'haskell': 0xD0A0FF, 'hs': 0xD0A0FF,
        'sql': 0xFF9900,
        'html': 0xFF5500, 'css': 0xFF5500,
        'fortran': 0x9A72FF, 'f90': 0x9A72FF,
        'assembly': 0xFFD080, 'asm': 0xFFD080,
        'cobol': 0x66AAFF, 'cbl': 0x66AAFF,
        'makefile': 0x00FF00, // Grouped with DevOps/Glue
        'json': 0x00FFFF, 'yaml': 0x00FFFF, 'yml': 0x00FFFF, 'xml': 0x00FFFF,
        'markdown': 0xFFFFE0, 'md': 0xFFFFE0, 'txt': 0xFFFFE0, 'csv': 0xFFFFE0,
        'dockerfile': 0x00B0FF, 'docker': 0x00B0FF,
        'bin': 0x505050, 'exe': 0x505050
    },

    /**
     * Resolves a language string to a Hex color.
     * Uses the Exo-Protocol (Deterministic Hash) for unknown extensions.
     */
    getLanguageColor: (langString) => {
        if (!langString) return 0xffffff;
        const normalized = langString.toLowerCase().trim();
        
        // 1. Standard Protocol Check
        if (Colors.LANGUAGES[normalized]) {
            return Colors.LANGUAGES[normalized];
        }

        // 2. Exo-Protocol (High-Contrast Hash)
        let hash = 0;
        for (let i = 0; i < normalized.length; i++) {
            hash = normalized.charCodeAt(i) + ((hash << 5) - hash);
        }
        
        const h = Math.abs(hash) % 360;
        const s = 80 + (Math.abs(hash >> 8) % 20);  // Locks Saturation 80-100%
        const l = 60 + (Math.abs(hash >> 16) % 20); // Locks Lightness 60-80%

        // Inline HSL to Hex Conversion
        const lNorm = l / 100;
        const a = (s / 100) * Math.min(lNorm, 1 - lNorm);
        const f = n => {
            const k = (n + h / 30) % 12;
            const color = lNorm - a * Math.max(Math.min(k - 3, 9 - k, 1), -1);
            return Math.round(255 * color).toString(16).padStart(2, '0');
        };
        return parseInt(`0x${f(0)}${f(8)}${f(4)}`, 16);
    },

    // 2. HUD LEGEND CONFIGURATION.
    LEGENDS: {
        cognitive_load: { 
            title: "Cognitive Load Exposure", 
            gradient: "linear-gradient(90deg, #ffffff 0%, #cc00ff 100%)", 
            bins: [20, 40, 60, 90], labels: ["VERY LOW", "LOW", "INTERMEDIATE", "HIGH", "VERY HIGH"],
            colors: ["#ffffff", "#d9b3ff", "#c666ff", "#cc00ff", "#9900cc"]
        },
        safety_score: { 
            title: "Safety Exposure", 
            gradient: "linear-gradient(90deg, #00f3ff 0%, #cc0000 100%)", 
            bins: [10, 40, 60, 80], labels: ["VERY LOW", "LOW", "INTERMEDIATE", "HIGH", "VERY HIGH"],
            colors: ["#00f3ff", "#7af9ff", "#ffffff", "#ff6666", "#cc0000"]
        },
        tech_debt: { 
            title: "Tech Debt Exposure", 
            gradient: "linear-gradient(90deg, #cccccc 0%, #0044cc 100%)",
            bins: [20, 40, 60, 80], labels: ["VERY LOW", "LOW", "INTERMEDIATE", "HIGH", "VERY HIGH"],
            colors: ["#ffffff", "#99b3ff", "#3377ff", "#1b57cf", "#0044cc"]        
        },
        verification: { 
            title: "Testing Exposure & Testing", 
            gradient: "linear-gradient(90deg, #cccccc 0%, #00b3b3 100%)", 
            bins: [10, 40, 60, 80], labels: ["IRONCLAD", "LOW", "MODERATE", "HIGH", "VERY HIGH"],
            colors: ["#ffffff", "#ccffff", "#66ffff", "#00e6e6", "#00b3b3"]
        },
        api_exposure: {
            title: "API Exposure",
            gradient: "linear-gradient(90deg, #ffffff 0%, #ff007f 100%)", 
            bins: [20, 40, 60, 80], labels: ["VERY LOW", "LOW", "MODERATE", "HIGH", "VERY HIGH"],
            colors: ["#ffffff", "#ffb3d9", "#ff66b3", "#ff007f", "#cc0066"]
        },
        concurrency: {
            title: "Concurrency Exposure",
            gradient: "linear-gradient(90deg, #ffffff 0%, #cc3700 100%)", 
            bins: [20, 50, 80], labels: ["LOW", "MODERATE", "HIGH", "VERY HIGH"],
            colors: ["#ffffff", "#ffccb3", "#ff9966", "#ff4500", "#cc3700"]
        },
        state_flux: {
            title: "State Flux Exposure",
            gradient: "linear-gradient(90deg, #ffffff 0%, #bfff00 100%)", 
            bins: [20, 40, 60, 80], labels: ["VERY LOW", "LOW", "MODERATE", "HIGH", "VERY HIGH"],
            colors: ["#ffffff", "#e6ff99", "#ccff33", "#bfff00", "#8cb300"]
        },
        graveyard: { 
            title: "Graveyard (Dead Code)", 
            gradient: "linear-gradient(90deg, #ffffff 0%, #483d8b 100%)", 
            bins: [10, 30, 50, 70], labels: ["CLEAN", "LOW", "INTERMEDIATE", "HIGH", "GRAVEYARD"],
            colors: ["#ffffff", "#ccd1e6", "#99a3cc", "#6675b3", "#483d8b"]
        },
        spec_match: {
            title: "Spec Alignment",
            gradient: "linear-gradient(90deg, #ffffff 0%, #0077ff 100%)", 
            bins: [20, 40, 60, 90], labels: ["HIGHLY ALIGNED", "ALIGNED", "MODERATE", "LOW", "VERY LOW"],
            colors: ["#ffffff", "#b3d9ff", "#66b3ff", "#1a8cff", "#0055b3"]
        },
        stability: {
            title: "Stability (Recent Commits)",
            bins: [20, 40, 60, 80], labels: ["HOT/NEW", "RECENT", "ACTIVE", "ESTABLISHED", "ENDURING"],
            gradient: "linear-gradient(90deg, #76ff03 0%, #00f3ff 100%)", 
            colors: ["#76ff03", "#58fc42", "#3bf981", "#1df6c0", "#00f3ff"]        
        },
        churn: { 
            title: "Deep Churn", 
            gradient: "linear-gradient(90deg, #ffffff 0%, #ff6d00 100%)", 
            bins: [20, 40, 60, 80], labels: ["STATIC", "SETTLED", "FLUID", "ACTIVE", "HIGHLY ACTIVE"],
            colors: ["#ffffff", "#ffd9b3", "#ffb366", "#ff8c1a", "#ff6d00"]
        },
        documentation: { 
            title: "Documentation Risk", 
            bins: [20, 40, 60, 90], labels: ["THOROUGH", "LOW", "MODERATE", "HIGH", "UNDOCUMENTED"],
            gradient: "linear-gradient(90deg, #ffd700 0%, #8da3bd 100%)", 
            colors: ["#ffd700", "#e2ca2f", "#c6bd5e", "#a9b08e", "#8da3bd"] 
        },
        ownership: { 
            title: "Authorship", 
            gradient: "linear-gradient(90deg, #00f3ff 0%, #ffffff 50%, #ff00ff 100%)", 
            bins: [20, 40, 60, 80], labels: ["INDIVIDUAL", "SMALL TEAM", "SQUAD", "DEPT", "COMMUNITY"],
            colors: ["#00f3ff", "#7af9ff", "#ffffff", "#ff7aff", "#ff00ff"]
        },
        civil_war: { 
            title: "Civil War", 
            gradient: "linear-gradient(90deg, #39ff14 0%, #0000ff 50%, #ffff00 100%)", 
            bins: [20, 80], labels: ["TABS", "MIXED", "SPACES"],
            colors: ["#39ff14", "#0000ff", "#ffff00"]
        }
    },

    // 3. THEME REGISTRY
    // Defines the "Basal States" of the universe
    THEMES: {
        'ice-crystal': {
            name: "Ice Crystal",
            description: "Minimalist.",
            bg: 0x020205,         
            fog: 0x0a0a15,         
            basalColor: 0xffffff,  
            basalVariance: [0xffffff, 0xadd8e6, 0xffe4e1, 0x87cefa, 0xffd1dc], 
            glowColor: 0xe0f7ff,   
            bloom: 1.2,
            dimmingFactor: 1.0,
            wire: false,
            stars: [0xffffff, 0xe0f7ff],
            lockColor: 0xffffff,
            diffuseBloom: 1.2,

            // v5.4 UI METADATA (Performance HUD Sync)
            uiAccent: "#ffffff",
            uiPanel: "rgba(2, 2, 5, 0.95)",
            uiText: "#ffffff"
        },
        'galactic': {
            name: "Galactic",
            description: "Colorfully Diverse & Vibrant.",
            bg: 0x050508,         
            fog: 0x050508,
            basalColor: 0x00f3ff,  
            basalPalette: [
                0xbc13fe, 0xffaa00, 0x00f3ff, 0xbfff00, 
                0xff00ff, 0x00ff00, 0xff0033, 0xffe600,
                0x2200ff, 0xffffff
            ],           
            glowColor: 0x00f3ff,
            bloom: 1.5,
            dimmingFactor: 0.2,
            wire: false,
            stars: [0x44aaff, 0xff44aa, 0xffffff],
            lockColor: null,       
            diffuseBloom: 1.5,

            // v5.4 UI METADATA (Performance HUD Sync)
            uiAccent: "#00f3ff",
            uiPanel: "rgba(5, 5, 8, 0.95)",
            uiText: "#00f3ff"
        },
        'matrix': {
            name: "The Matrix",
            description: "Hacker Aesthetic.",
            bg: 0x000000,         
            fog: 0x000000,
            basalColor: 0x00ff41,  
            basalVariance: [0x00ff41, 0x00dd33, 0x00bb22], 
            glowColor: 0x00ff41,
            bloom: 2.0,            
            dimmingFactor: 0.1,    
            wire: true,            
            stars: [0x00ff41, 0x00aa00],
            lockColor: 0x00ff41,
            diffuseBloom: 2.0,

            // v5.4 UI METADATA (Performance HUD Sync)
            uiAccent: "#00ff41",
            uiPanel: "rgba(0, 0, 0, 0.95)",
            uiText: "#00ff41"
        },
        'high-vis': {
            name: "High-Visibility",
            description: "Monochrome / A11y.",
            bg: 0xffffff,           // Pure White Background
            fog: 0xffffff,          // Pure White Fog
            basalColor: 0x000000,   // BLACK Geometry (Was Orange)
            glowColor: 0x000000,    // BLACK Glow (No bloom, just solid)
            bloom: 0.0,            
            dimmingFactor: 1.0,    
            wire: true,             // Wireframe mode for sharp lines
            stars: [0x000000],      // Black stars
            lockColor: 0x000000,    // Black selection color
            diffuseBloom: 0.0,

            // v5.4 UI METADATA (Strict Black & White)
            uiAccent: "#000000",    // Black UI Accents
            uiPanel: "#ffffff",     // White Panels
            uiText: "#000000"       // Black Text
        }
    },

    // 4. UTILITY METHODS
    
    /**
     * Deterministic color hashing for Authors (Ownership Mode)
     */
    getAuthorColor: (name) => {
        let hash = 0;
        for (let i = 0; i < name.length; i++) {
            hash = name.charCodeAt(i) + ((hash << 5) - hash);
        }
        const color = (hash & 0x00FFFFFF).toString(16).toUpperCase();
        return parseInt("00000".substring(0, 6 - color.length) + color, 16);
    },

    /**
     * Maps a score (0-100) to a specific behavioral color key
     */
    getMetricColor: (mode, score) => {
            const C = Colors.BEHAVIOR;

            if (mode === 'none' || mode === 'default') return C.standard;

            switch(mode) {
                case 'cognitive_load': 
                    return score > 70 ? C.cognitive_purple : 0xffffff;
                
                case 'safety': 
                    // High risk = Crimson, Low risk = Cyan
                    return score > 60 ? C.safety_crimson : (score < 40 ? C.shield_cyan : 0xffffff);
                
                case 'debt': 
                    return score > 50 ? C.debt_blue : 0xffffff;
                
                case 'coverage': // Verification
                    return score > 60 ? C.verification_teal : 0xffffff;
                
                case 'api': // Added missing metric
                    return score > 60 ? C.api_rose : 0xffffff;
                
                case 'concurrency': // Added missing metric
                    return score > 50 ? C.concurrency_uv : 0xffffff;
                
                case 'flux': // Added missing metric
                    return score > 60 ? C.flux_lime : 0xffffff;
                
                case 'graveyard': // Added missing metric
                    return score > 50 ? C.graveyard_slate : 0xffffff;
                
                case 'spec_match': 
                    return score > 20 ? C.spec_blue : 0xffffff;
                
                case 'stability': 
                    // Low score (Hot/New) = Green, High score (Enduring) = White
                    return score < 30 ? C.stability_green : 0x00f3ff;
                
                case 'churn': 
                    return score > 60 ? C.churn_orange : 0xffffff;
                
                case 'docs': 
                    // High exposure = Umber, Encyclopedic = Gold
                    return score > 60 ? C.docs_umber : (score < 40 ? C.docs_gold : 0xffffff);
                
                case 'indentation': // Civil War
                    if (score < 20) return C.tabs_green; 
                    if (score > 80) return C.spaces_yellow;     
                    return C.mixed_blue;
                
                case 'ownership': 
                    // High ownership = Pink, Low ownership = Cyan
                    return score > 70 ? C.coverage_pink : (score < 40 ? C.shield_cyan : 0xffffff);
                
                default: 
                    return 0xffffff;
            }
    }
};

// --- SMART LEGEND INTERCEPTOR (HIGH-VIS ACCESSIBILITY) ---
// Automatically overrides gradients and HUD colors when Theme 4 is active.
Object.keys(Colors.LEGENDS).forEach(key => {
    const standardGradient = Colors.LEGENDS[key].gradient;
    const standardColors = Colors.LEGENDS[key].colors;
    
    // 1. Override the CSS Gradient for the top legend
    if (standardGradient) {
        Object.defineProperty(Colors.LEGENDS[key], 'gradient', {
            get: function() {
                if (window.App && window.App.engine && window.App.engine.uThemeIndex.value === 4) {
                    // 5-Stop CSS Gradient matching the GPU
                    return "linear-gradient(90deg, #000000 0%, #008080 25%, #0000ff 50%, #ff00ff 75%, #ff0000 100%)";
                }
                return standardGradient;
            }
        });
    }

    // 2. Override the discrete colors for the individual File HUD stats
    if (standardColors) {
        Object.defineProperty(Colors.LEGENDS[key], 'colors', {
            get: function() {
                if (window.App && window.App.engine && window.App.engine.uThemeIndex.value === 4) {
                    // 5-stop array: Black -> Dark Teal -> Blue -> Magenta -> Red
                    const highVisColors = ["#000000", "#008080", "#0000ff", "#ff00ff", "#ff0000"];
                    // Slice the array so it matches the length of the original schema
                    return highVisColors.slice(0, standardColors.length);
                }
                return standardColors;
            }
        });
    }
});

window.Colors = Colors;