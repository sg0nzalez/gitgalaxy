/**
 * GitGalaxy
 * Copyright (c) 2026 Joe Esquibel
 *
 * This source code is licensed under the PolyForm Noncommercial License 1.0.0.
 * You may not use this file except in compliance with the License.
 * A copy of the license can be found in the LICENSE file in the root directory
 * of this project, or at https://polyformproject.org/licenses/noncommercial/1.0.0/
 */
import { 
    uniform, attribute, float, color, mix, vec4,
    instanceIndex, select, hash, time, sin, mul, 
    dot, vec3, max, pow, distance, cameraPosition, positionWorld, varying 
} from 'three/tsl';

/**
 * FILENAME: phase-6-shaders.js
 * Phase 6: Visual Themes TSL Implementation
 * Vector Packed & Varying-Optimized for Mobile WebGPU Compatibility
 */

export const createPhase6Shaders = (engine) => {
    // 1. Uniforms
    const uThemeIndex = engine.uThemeIndex || uniform(0);
    const uMetricMode = engine.uMetricMode || uniform(0);
    const uTime = time;
    const uSelectedGlobalId = engine.uSelectedGlobalId || uniform(-1.0);
    const uSelectedConstellationId = engine.uSelectedConstellationId || uniform(-1.0);
    const uMoonFadeDist = engine.uMoonFadeDist || uniform(5000.0);

    // =====================================================================
    // 2. ATTRIBUTES: VECTOR PACKED DATA
    // We use exactly 6 custom buffers. Combined with Position and Matrix,
    // this hits the exact 8-buffer mobile GPU limit.
    // =====================================================================
    const aRiskPack1 = attribute('aRiskPack1', 'vec4');
    const aRiskPack2 = attribute('aRiskPack2', 'vec4');
    const aRiskPack3 = attribute('aRiskPack3', 'vec4');
    const aRiskPack4 = attribute('aRiskPack4', 'vec4'); 
    const aRiskPack5 = attribute('aRiskPack5', 'vec4'); 
    const aMetaPack1 = attribute('aMetaPack1', 'vec4');

    // 3. Unpack Vectors into Variables
    const aCognitive = aRiskPack1.x;       
    const aSafety = aRiskPack1.y;          
    const aDebt = aRiskPack1.z;            
    const aVerification = aRiskPack1.w;    
    const aApi = aRiskPack2.x;             
    const aConcurrency = aRiskPack2.y;     
    const aFlux = aRiskPack2.z;            
    const aGraveyard = aRiskPack2.w;       
    const aSpec = aRiskPack3.x;            
    const aStability = aRiskPack3.y;       
    const aChurn = aRiskPack3.z;           
    const aDocs = aRiskPack3.w;            
    
    // NEW: SECURITY LENS VARIABLES
    const aObscured = aRiskPack4.x;
    const aLogicBomb = aRiskPack4.y;
    const aInjection = aRiskPack4.z;
    const aMemory = aRiskPack4.w;
    // UNPACKING SQUASHED BUFFERS
    const aSecrets = aRiskPack5.x;
    const aLangColor = vec3(aRiskPack5.y, aRiskPack5.z, aRiskPack5.w);
    
    // UNPACKING THE META SUITCASE
    const aCivilWar = aMetaPack1.x;          
    const aPopularity = aMetaPack1.y;        
    const aGlobalId = aMetaPack1.z;          
    const aConstellationId = aMetaPack1.w;       

    // 4. Ice Crystal Theme
    const iceSeed = hash(instanceIndex.add(1.0));
    let iceColor = color(0xffffff);
    iceColor = select(iceSeed.greaterThan(0.2), color(0xadd8e6), iceColor);
    iceColor = select(iceSeed.greaterThan(0.4), color(0xffe4e1), iceColor);
    iceColor = select(iceSeed.greaterThan(0.6), color(0x87cefa), iceColor);
    iceColor = select(iceSeed.greaterThan(0.8), color(0xffd1dc), iceColor);

    // 5. Galactic Theme
    const gSeed = hash(instanceIndex.mul(1.5));
    let galacticColor = color(0xbc13fe); 
    galacticColor = select(gSeed.greaterThan(0.1), color(0xffaa00), galacticColor); 
    galacticColor = select(gSeed.greaterThan(0.2), color(0x00f3ff), galacticColor); 
    galacticColor = select(gSeed.greaterThan(0.3), color(0xbfff00), galacticColor); 
    galacticColor = select(gSeed.greaterThan(0.4), color(0xff00ff), galacticColor); 
    galacticColor = select(gSeed.greaterThan(0.5), color(0x00ff00), galacticColor); 
    galacticColor = select(gSeed.greaterThan(0.6), color(0xff0033), galacticColor); 
    galacticColor = select(gSeed.greaterThan(0.7), color(0xffe600), galacticColor); 
    galacticColor = select(gSeed.greaterThan(0.8), color(0x2200ff), galacticColor); 
    galacticColor = select(gSeed.greaterThan(0.9), color(0xffffff), galacticColor); 

    // 6. Matrix Theme 
    const matrixSeed = hash(instanceIndex.add(2.0));
    let matrixColor = color(0x00ff41);
    matrixColor = select(matrixSeed.greaterThan(0.33), color(0x00dd33), matrixColor);
    matrixColor = select(matrixSeed.greaterThan(0.66), color(0x00bb22), matrixColor);

    // 7. High-Vis Theme 
    const highVisColor = color(0x000000); 

    // 8. Final Theme Selection
    const themeColor = select(
        uThemeIndex.equal(4), highVisColor,
        select(
            uThemeIndex.equal(3), matrixColor,
            select(uThemeIndex.equal(2), galacticColor, iceColor) 
        )
    );

    // 9. ABSOLUTE GRADIENT MAPPING
    const cWhite = color(0xffffff);
    const mMax = {
        cog: color(0xcc00ff), saf: color(0xcc0000), debt: color(0x0044cc),  
        ver: color(0x00b3b3), api: color(0xff007f), conc: color(0xcc3700),  
        flux: color(0xbfff00), grave: color(0x483d8b), spec: color(0x0077ff),  
        stab: color(0x00f3ff), chu: color(0xff6d00), docs: color(0x8da3bd), civil: color(0xffff00)  
    };

    const mMin = {
        cog: cWhite, saf: color(0x00f3ff), debt: cWhite,
        ver: cWhite, api: cWhite, conc: cWhite,
        flux: cWhite, grave: cWhite, spec: cWhite,
        stab: color(0x76ff03), chu: cWhite, docs: color(0xffd700), civil: color(0x39ff14)  
    };

    // =====================================================================
    // 10. Extract Relevance for the Active Mode
    // MOBILE SHADER FIX: Grouped into chunks to prevent AST Stack Overflow on mobile GPUs.
    // =====================================================================
    const rel1 = select(uMetricMode.equal(1), aCognitive, 
                 select(uMetricMode.equal(2), aSafety, 
                 select(uMetricMode.equal(3), aDebt, 
                 select(uMetricMode.equal(4), aVerification, 
                 select(uMetricMode.equal(5), aApi, float(0))))));

    const rel2 = select(uMetricMode.equal(6), aConcurrency,
                 select(uMetricMode.equal(7), aFlux,
                 select(uMetricMode.equal(8), aGraveyard,
                 select(uMetricMode.equal(9), aSpec,
                 select(uMetricMode.equal(10), aStability, float(0))))));

    const rel3 = select(uMetricMode.equal(11), aChurn,
                 select(uMetricMode.equal(12), aDocs,
                 select(uMetricMode.equal(13), aCivilWar,
                 select(uMetricMode.equal(14), float(1.0),
                 select(uMetricMode.equal(15), aObscured, float(0))))));

    const rel4 = select(uMetricMode.equal(16), aLogicBomb,
                 select(uMetricMode.equal(17), aInjection,
                 select(uMetricMode.equal(18), aMemory,
                 select(uMetricMode.equal(19), aSecrets, float(0)))));

    const relevance = rel1.add(rel2).add(rel3).add(rel4);

    // =====================================================================
    // 11. Select Min and Max Colors dynamically
    // =====================================================================
    const secMax = color(0xcc0000); // Red
    const secMin = color(0x00f3ff); // Cyan/Teal
    const cBlack = color(0x000000); // Baseline zero

    const max1 = select(uMetricMode.equal(1), mMax.cog,
                 select(uMetricMode.equal(2), mMax.saf,
                 select(uMetricMode.equal(3), mMax.debt,
                 select(uMetricMode.equal(4), mMax.ver,
                 select(uMetricMode.equal(5), mMax.api, cBlack)))));

    const max2 = select(uMetricMode.equal(6), mMax.conc,
                 select(uMetricMode.equal(7), mMax.flux,
                 select(uMetricMode.equal(8), mMax.grave,
                 select(uMetricMode.equal(9), mMax.spec,
                 select(uMetricMode.equal(10), mMax.stab, cBlack)))));

    const max3 = select(uMetricMode.equal(11), mMax.chu,
                 select(uMetricMode.equal(12), mMax.docs,
                 select(uMetricMode.equal(13), mMax.civil, cBlack)));

    const max4 = select(uMetricMode.greaterThan(14), secMax, cBlack);

    // Sum the chunks, then fallback to theme color if no metric (0) or language identity (14) is active
    let maxC = max1.add(max2).add(max3).add(max4);
    maxC = select(uMetricMode.equal(0), themeColor, maxC);
    maxC = select(uMetricMode.equal(14), themeColor, maxC); 

    const min1 = select(uMetricMode.equal(1), mMin.cog,
                 select(uMetricMode.equal(2), mMin.saf,
                 select(uMetricMode.equal(3), mMin.debt,
                 select(uMetricMode.equal(4), mMin.ver,
                 select(uMetricMode.equal(5), mMin.api, cBlack)))));

    const min2 = select(uMetricMode.equal(6), mMin.conc,
                 select(uMetricMode.equal(7), mMin.flux,
                 select(uMetricMode.equal(8), mMin.grave,
                 select(uMetricMode.equal(9), mMin.spec,
                 select(uMetricMode.equal(10), mMin.stab, cBlack)))));

    const min3 = select(uMetricMode.equal(11), mMin.chu,
                 select(uMetricMode.equal(12), mMin.docs,
                 select(uMetricMode.equal(13), mMin.civil, cBlack)));

    const min4 = select(uMetricMode.greaterThan(14), secMin, cBlack);

    let minC = min1.add(min2).add(min3).add(min4);
    minC = select(uMetricMode.equal(0), themeColor, minC);
    minC = select(uMetricMode.equal(14), themeColor, minC);

    // 12. Calculate Interpolation
    const curvedRelevance = pow(relevance, float(2.0));
    let gradientColor = mix(minC, maxC, curvedRelevance);

    const civilBlue = color(0x0000ff);
    const civilColor = select(relevance.lessThan(0.5), mix(mMin.civil, civilBlue, relevance.mul(2.0)), mix(civilBlue, mMax.civil, relevance.sub(0.5).mul(2.0)));
    gradientColor = select(uMetricMode.equal(13), civilColor, gradientColor);

    const hvBlack = color(0x000000);  
    const hvTeal  = color(0x008080);   
    const hvBlue  = color(0x0000ff);   
    const hvPink  = color(0xff00ff);   
    const hvRed   = color(0xff0000);   
    const highVisGradient = select(relevance.lessThan(0.25), mix(hvBlack, hvTeal, relevance.mul(4.0)), select(relevance.lessThan(0.5), mix(hvTeal, hvBlue, relevance.sub(0.25).mul(4.0)), select(relevance.lessThan(0.75), mix(hvBlue, hvPink, relevance.sub(0.5).mul(4.0)), mix(hvPink, hvRed, relevance.sub(0.75).mul(4.0)))));
    
    gradientColor = select(uThemeIndex.equal(4), highVisGradient, gradientColor);
    gradientColor = select(uMetricMode.equal(14), aLangColor, gradientColor);    

    // =====================================================================
    // 🚨 THE POTATO-GPU VARYING FIX 🚨
    // We force all attribute-heavy math into the Vertex Shader using varying().
    // This drops the varying count from 25+ down to just 4!
    // It ALSO keeps aGlobalId in 32-bit precision, fixing the selection bug!
    // =====================================================================
    const vGradientColor = varying(gradientColor);
    const vThemeColor = varying(themeColor);
    const vPopularity = varying(aPopularity);
    const vTwinkleSeed = varying(hash(instanceIndex.add(42.0)));

    // --- 13. Glow & Pulse ---
    let baseGlow = float(2.0); 
    baseGlow = select(uThemeIndex.equal(2), float(2.5), baseGlow); 
    baseGlow = select(uThemeIndex.equal(3), float(2.2), baseGlow); 
    baseGlow = select(uThemeIndex.equal(4), float(0.0), baseGlow); 
    
    const popularityGlowBoost = vPopularity.mul(float(3.0));
    let idleGlow = baseGlow.add(popularityGlowBoost);

    const pulseFreq = mix(float(0.3), float(0.8), vTwinkleSeed).add(vPopularity.mul(float(1.5))); 
    const timeOffset = vTwinkleSeed.mul(100.0); 
    const wave = sin(mul(uTime.add(timeOffset), pulseFreq)).mul(0.5).add(0.5); 
    const idlePulse = mix(idleGlow, idleGlow.add(1.0), wave);

    const phosphorBlend = wave.mul(0.05); 
    const crtColor = mix(vThemeColor, color(0xffffff), phosphorBlend);
    const finalThemeColor = select(uThemeIndex.equal(3), crtColor, vThemeColor);
    const glowingThemeColor = finalThemeColor.mul(idlePulse);

    const bloomWeights = vec3(0.2126, 0.7152, 0.0722); 
    const currentLuma = max(dot(vGradientColor, bloomWeights), float(0.15)); 
    const targetLuma = mix(float(1.4), float(2.2), wave); 
    const adaptiveGlowColor = vGradientColor.mul(targetLuma.div(currentLuma));

    let finalColor = select(uMetricMode.greaterThan(0), adaptiveGlowColor, glowingThemeColor);
    finalColor = finalColor.mul(1.25); 
    finalColor = select(uThemeIndex.equal(4), select(uMetricMode.greaterThan(0), vGradientColor, vThemeColor), finalColor);

    // --- 14. ROBUST GLOBAL DIMMING LOGIC ---
    let baseOpacity = float(0.8);
    const fConstId = float(uSelectedConstellationId);
    const fGlobalId = float(uSelectedGlobalId);

    const isConstActive = fConstId.greaterThan(-0.5);
    const inConstellation = aConstellationId.sub(fConstId).abs().lessThan(0.5);
    let finalOpacity = select(isConstActive, select(inConstellation, float(0.9), float(0.05)), baseOpacity);

    const isStarActive = fGlobalId.greaterThan(-0.5);
    const isTargetStar = aGlobalId.sub(fGlobalId).abs().lessThan(0.5);
    finalOpacity = select(isStarActive, select(isConstActive, finalOpacity, select(isTargetStar, float(0.9), float(0.05))), finalOpacity);

    // --- 15. ATMOSPHERIC DISSOLVE (MOONS) ---
    const distToCam = distance(cameraPosition, positionWorld);
    const distRatio = distToCam.div(uMoonFadeDist);
    const falloff = float(1.0).sub(pow(distRatio, 2.0));
    const baseMoonOpacity = max(float(0.0), falloff).mul(0.8);
    
    const finalMoonOpacity = select(isTargetStar, float(0.8), baseMoonOpacity);
    const dimmedMoonOpacity = select(isConstActive, select(inConstellation, finalMoonOpacity, float(0.01)), finalMoonOpacity);
    let superDimmedMoonOpacity = select(isStarActive, select(isConstActive, dimmedMoonOpacity, select(isTargetStar, finalMoonOpacity, float(0.01))), dimmedMoonOpacity);
    
    // High-Vis dynamic override
    finalOpacity = select(uThemeIndex.equal(4), float(1.0), finalOpacity);
    superDimmedMoonOpacity = select(uThemeIndex.equal(4), float(1.0), superDimmedMoonOpacity);

    // Lock Opacities to the Vertex Shader
    const vFinalOpacity = varying(finalOpacity);
    const vMoonOpacity = varying(superDimmedMoonOpacity);

    return {
        colorNode: finalColor,
        opacityNode: vFinalOpacity,
        moonOpacityNode: vMoonOpacity
    };
};
    let baseGlow = float(2.0); 
    baseGlow = select(uThemeIndex.equal(2), float(2.5), baseGlow); 
    baseGlow = select(uThemeIndex.equal(3), float(2.2), baseGlow); 
    baseGlow = select(uThemeIndex.equal(4), float(0.0), baseGlow); 
    
    // We use `aPopularity` natively now
    const popularityGlowBoost = aPopularity.mul(float(3.0));
    let idleGlow = baseGlow.add(popularityGlowBoost);

    const twinkleSeed = hash(instanceIndex.add(42.0));
    const pulseFreq = mix(float(0.3), float(0.8), twinkleSeed).add(aPopularity.mul(float(1.5))); 
    const timeOffset = twinkleSeed.mul(100.0); 
    const wave = sin(mul(uTime.add(timeOffset), pulseFreq)).mul(0.5).add(0.5); 
    const idlePulse = mix(idleGlow, idleGlow.add(1.0), wave);

    const phosphorBlend = wave.mul(0.05); 
    const crtColor = mix(themeColor, color(0xffffff), phosphorBlend);
    const finalThemeColor = select(uThemeIndex.equal(3), crtColor, themeColor);
    const glowingThemeColor = finalThemeColor.mul(idlePulse);

    const bloomWeights = vec3(0.2126, 0.7152, 0.0722); 
    const currentLuma = max(dot(gradientColor, bloomWeights), float(0.15)); 
    const targetLuma = mix(float(1.4), float(2.2), wave); 
    const adaptiveGlowColor = gradientColor.mul(targetLuma.div(currentLuma));

    let finalColor = select(uMetricMode.greaterThan(0), adaptiveGlowColor, glowingThemeColor);
    finalColor = finalColor.mul(1.25); 
    finalColor = select(uThemeIndex.equal(4), select(uMetricMode.greaterThan(0), gradientColor, themeColor), finalColor);

    // --- 14. ROBUST GLOBAL DIMMING LOGIC ---
    let baseOpacity = float(0.8);
    const fConstId = float(uSelectedConstellationId);
    const fGlobalId = float(uSelectedGlobalId);

    const isConstActive = fConstId.greaterThan(-0.5);
    
    // .abs().lessThan(0.5) provides a safe 0.5 margin of error for float math
    const inConstellation = aConstellationId.sub(fConstId).abs().lessThan(0.5);
    let finalOpacity = select(isConstActive, select(inConstellation, float(0.9), float(0.05)), baseOpacity);

    const isStarActive = fGlobalId.greaterThan(-0.5);
    const isTargetStar = aGlobalId.sub(fGlobalId).abs().lessThan(0.5);
    finalOpacity = select(isStarActive, select(isConstActive, finalOpacity, select(isTargetStar, float(0.9), float(0.05))), finalOpacity);

    // --- 15. ATMOSPHERIC DISSOLVE (MOONS) ---
    const distToCam = distance(cameraPosition, positionWorld);
    const distRatio = distToCam.div(uMoonFadeDist);
    const falloff = float(1.0).sub(pow(distRatio, 2.0));
    const baseMoonOpacity = max(float(0.0), falloff).mul(0.8);
    
    const finalMoonOpacity = select(isTargetStar, float(0.8), baseMoonOpacity);
    const dimmedMoonOpacity = select(isConstActive, select(inConstellation, finalMoonOpacity, float(0.01)), finalMoonOpacity);
    let superDimmedMoonOpacity = select(isStarActive, select(isConstActive, dimmedMoonOpacity, select(isTargetStar, finalMoonOpacity, float(0.01))), dimmedMoonOpacity);
    
    // High-Vis dynamic override
    finalOpacity = select(uThemeIndex.equal(4), float(1.0), finalOpacity);
    superDimmedMoonOpacity = select(uThemeIndex.equal(4), float(1.0), superDimmedMoonOpacity);

    return {
        colorNode: finalColor,
        opacityNode: finalOpacity,
        moonOpacityNode: superDimmedMoonOpacity
    };
};