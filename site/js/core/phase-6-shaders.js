import { 
    uniform, attribute, float, color, mix, vec4,
    instanceIndex, select, hash, time, sin, mul, 
    dot, vec3, max, pow, distance, cameraPosition, positionWorld, varying,
    floor, fract
} from 'three/tsl';

export const createPhase6Shaders = (engine) => {
    // 1. Uniforms
    const uThemeIndex = engine.uThemeIndex || uniform(0);
    const uMetricMode = engine.uMetricMode || uniform(0);
    const uTime = time;
    const uSelectedGlobalId = engine.uSelectedGlobalId || uniform(-1.0);
    const uSelectedConstellationId = engine.uSelectedConstellationId || uniform(-1.0);
    const uMoonFadeDist = engine.uMoonFadeDist || uniform(5000.0);

    // =====================================================================
    // 2. ATTRIBUTES: THE RAW DATA
    // =====================================================================
    const aRiskPack1 = attribute('aRiskPack1', 'vec4');
    const aRiskPack2 = attribute('aRiskPack2', 'vec4');
    const aRiskPack3 = attribute('aRiskPack3', 'vec4');
    const aRiskPack4 = attribute('aRiskPack4', 'vec4'); 
    const aRiskPack5 = attribute('aRiskPack5', 'vec4'); 
    const aMetaPack1 = attribute('aMetaPack1', 'vec4');

    // =====================================================================
    // 🚨 THE EXPLICIT VARYING SUITCASE 🚨
    // =====================================================================
    const vRiskPack1 = varying(aRiskPack1);
    const vRiskPack2 = varying(aRiskPack2);
    const vRiskPack3 = varying(aRiskPack3);
    const vRiskPack4 = varying(aRiskPack4);
    const vRiskPack5 = varying(aRiskPack5);
    const vMetaPack1 = varying(aMetaPack1);
    const vInstIndex = varying(float(instanceIndex));

    // 3. Unpack Vectors into Variables (Executing safely in the Fragment Shader)
    const aCognitive = vRiskPack1.x;       
    const aSafety = vRiskPack1.y;          
    const aDebt = vRiskPack1.z;            
    const aVerification = vRiskPack1.w;    
    const aApi = vRiskPack2.x;             
    const aConcurrency = vRiskPack2.y;     
    const aFlux = vRiskPack2.z;            
    const aGraveyard = vRiskPack2.w;       
    const aSpec = vRiskPack3.x;            
    const aStability = vRiskPack3.y;       
    const aChurn = vRiskPack3.z;           
    const aDocs = vRiskPack3.w;            
    
    const aObscured = vRiskPack4.x;
    const aLogicBomb = vRiskPack4.y;
    const aInjection = vRiskPack4.z;
    const aMemory = vRiskPack4.w;

    const aSecrets = vRiskPack5.x;
    const aLangColor = vec3(vRiskPack5.y, vRiskPack5.z, vRiskPack5.w);
    
    // =================================================================
    // 🚨 DATA UNPACKING: BUFFER OVERFLOW PREVENTION 🚨
    // We retrieve the integer (Cluster ID) and decimal (Popularity) from the 
    // single compressed float. This trick saves an entire vertex buffer binding,
    // preventing silent mobile GPU crashes.
    // =================================================================
    const aCivilWar = vMetaPack1.x;          
    const packedMeta = vMetaPack1.y;
    const aPopularity = fract(packedMeta);        
    const aClusterId = floor(packedMeta);
    const aGlobalId = vMetaPack1.z;          
    const aConstellationId = vMetaPack1.w;

    // 4. Ice Crystal Theme
    const iceSeed = hash(vInstIndex.add(1.0));
    let iceColor = color(0xffffff);
    iceColor = select(iceSeed.greaterThan(0.2), color(0xadd8e6), iceColor);
    iceColor = select(iceSeed.greaterThan(0.4), color(0xffe4e1), iceColor);
    iceColor = select(iceSeed.greaterThan(0.6), color(0x87cefa), iceColor);
    iceColor = select(iceSeed.greaterThan(0.8), color(0xffd1dc), iceColor);

    // 5. Galactic Theme
    const gSeed = hash(vInstIndex.mul(1.5));
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
    const matrixSeed = hash(vInstIndex.add(2.0));
    let matrixColor = color(0x00ff41);
    matrixColor = select(matrixSeed.greaterThan(0.33), color(0x00dd33), matrixColor);
    matrixColor = select(matrixSeed.greaterThan(0.66), color(0x00bb22), matrixColor);

    // 7. High-Vis Theme 
    const highVisColor = color(0xffffff);

    // 8. Final Theme Selection
    const themeColor = select(
        uThemeIndex.equal(4), highVisColor,
        select(
            uThemeIndex.equal(3), matrixColor,
            select(uThemeIndex.equal(2), galacticColor, iceColor) 
        )
    );

    // =================================================================
    // 9. EXTRACT RELEVANCE SCORE FOR ACTIVE METRIC
    // =================================================================
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

    // =================================================================
    // 10. THE UNIVERSAL "TURBO" SPECTRUM MAPPER
    // =================================================================
    const cBlue   = color(0x0055ff);  
    const cCyan   = color(0x00ffff);   
    const cYellow = color(0xffff00);   
    const cOrange = color(0xff8800);   
    const cRed    = color(0xff0000);   
    
    let gradientColor = select(
        relevance.lessThan(0.25), mix(cBlue, cCyan, relevance.mul(4.0)), 
        select(
            relevance.lessThan(0.5), mix(cCyan, cYellow, relevance.sub(0.25).mul(4.0)), 
            select(
                relevance.lessThan(0.75), mix(cYellow, cOrange, relevance.sub(0.5).mul(4.0)), 
                mix(cOrange, cRed, relevance.sub(0.75).mul(4.0))
            )
        )
    );

    // EXCEPTION A: Civil War (Mode 13) gets a diverging Green -> Blue -> Yellow spectrum
    const civilBlue = color(0x0000ff);
    const civilMin = color(0x39ff14);
    const civilMax = color(0xffff00);
    const civilColor = select(relevance.lessThan(0.5), mix(civilMin, civilBlue, relevance.mul(2.0)), mix(civilBlue, civilMax, relevance.sub(0.5).mul(2.0)));
    gradientColor = select(uMetricMode.equal(13), civilColor, gradientColor);

    // EXCEPTION B: Language Identity (Mode 14) gets raw categorical hex colors
    gradientColor = select(uMetricMode.equal(14), aLangColor, gradientColor);

    // EXCEPTION C: Base State (Mode 0) falls back to the native environment Theme Color
    gradientColor = select(uMetricMode.equal(0), themeColor, gradientColor);

    // EXCEPTION D: File Architecture (Mode 20) gets 16 categorical colors
    const archColor = select(aClusterId.equal(0), color(0xFF3B30),
                      select(aClusterId.equal(1), color(0xFF9500),
                      select(aClusterId.equal(2), color(0xFFCC00),
                      select(aClusterId.equal(3), color(0xFFEE58),
                      select(aClusterId.equal(4), color(0xA4E720),
                      select(aClusterId.equal(5), color(0x28CD41),
                      select(aClusterId.equal(6), color(0x00C7BE),
                      select(aClusterId.equal(7), color(0x59C8FA),
                      select(aClusterId.equal(8), color(0x007AFF),
                      select(aClusterId.equal(9), color(0x5856D6),
                      select(aClusterId.equal(10), color(0xAF52DE),
                      select(aClusterId.equal(11), color(0xFF2D55),
                      select(aClusterId.equal(12), color(0xF9A8D4),
                      select(aClusterId.equal(13), color(0xE5E5EA),
                      select(aClusterId.equal(14), color(0xA2845E),
                      color(0x64748B)))))))))))))))); // Fallback to 15 (Slate Gray)

    gradientColor = select(uMetricMode.equal(20), archColor, gradientColor);

    // --- 13. Glow & Pulse ---
    let baseGlow = float(2.0); 
    baseGlow = select(uThemeIndex.equal(2), float(2.5), baseGlow); 
    baseGlow = select(uThemeIndex.equal(3), float(2.2), baseGlow); 
    baseGlow = select(uThemeIndex.equal(4), float(0.0), baseGlow); 
    
    const popularityGlowBoost = aPopularity.mul(float(3.0));
    let idleGlow = baseGlow.add(popularityGlowBoost);

    const twinkleSeed = hash(vInstIndex.add(42.0));
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
    
    // 🚨 THE FIX: If High-Vis mode AND no metric is selected (Mode 0), make the orbs flat white.
    // If a metric IS selected, allow the new A11y rainbow gradient to render!
    finalColor = select(
        uThemeIndex.equal(4), 
        select(uMetricMode.equal(0), color(0xffffff), finalColor), 
        finalColor
    );

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

    return {
        colorNode: finalColor,
        opacityNode: finalOpacity,
        moonOpacityNode: superDimmedMoonOpacity
    };
};