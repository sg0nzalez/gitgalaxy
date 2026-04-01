# Claim 4 (Comparing Languages)

If I have an engine that can scan and compare codebases across time and language, independent of compilation, I don't know about you but I want to take it for a spin! What patterns will emerge as we compare repos of python, COBOL and typescript? This is my current validation/proof of principle data set. I've analyzed 104 code bases and score them according to the blAST engine's risk exposure metrics and present it publically for validation and criticism. Openness and public input is the only way forward with a system like this. The following ridge line plots visualize the distribution of risk exposures and other metrics across languages. Please note, this data set needs to grow and likely has non-representative numbers of repos per language (3-10). Once I get a better automated pipeline going, I hope to automate the scanning of repos to get more representative distributions. The population distributions also clearly highlight that some of my risk exposure metrics are not dialed in well, like concurrency, these should produce ranges not be binary on/off measures. I have currently set the security measures to be very sensitive so normal coding practices are being listed as security warnings, but the sensitivity of these detections can be tuned down for a less annoying workflow and then turned back to --paranoid for your final sanity check before pushing it live.

*Click on any image to view it at full resolution.*

## Core Security & Vulnerability Risks

<table style="width:100%; text-align:center;">
  <tr>
    <td>
      <a href="../assets/analyses_ridgeplots/risk_hardcoded_payload_artifacts_ridgeplot.png">
        <img src="../assets/analyses_ridgeplots/risk_hardcoded_payload_artifacts_ridgeplot.png" width="300" loading="lazy" alt="Hardcoded Payload Artifacts"/><br/>
        <b>Hardcoded Payload Artifacts</b>
      </a>
    </td>
    <td>
      <a href="../assets/analyses_ridgeplots/risk_obfuscation_and_evasion_surface_ridgeplot.png">
        <img src="../assets/analyses_ridgeplots/risk_obfuscation_and_evasion_surface_ridgeplot.png" width="300" loading="lazy" alt="Obfuscation & Evasion Surface"/><br/>
        <b>Obfuscation & Evasion Surface</b>
      </a>
    </td>
    <td>
      <a href="../assets/analyses_ridgeplots/risk_exploit_generation_surface_ridgeplot.png">
        <img src="../assets/analyses_ridgeplots/risk_exploit_generation_surface_ridgeplot.png" width="300" loading="lazy" alt="Exploit Generation Surface"/><br/>
        <b>Exploit Generation Surface</b>
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="../assets/analyses_ridgeplots/risk_weaponizable_injection_vectors_ridgeplot.png">
        <img src="../assets/analyses_ridgeplots/risk_weaponizable_injection_vectors_ridgeplot.png" width="300" loading="lazy" alt="Weaponizable Injection Vectors"/><br/>
        <b>Weaponizable Injection Vectors</b>
      </a>
    </td>
    <td>
      <a href="../assets/analyses_ridgeplots/risk_raw_memory_manipulation_ridgeplot.png">
        <img src="../assets/analyses_ridgeplots/risk_raw_memory_manipulation_ridgeplot.png" width="300" loading="lazy" alt="Raw Memory Manipulation"/><br/>
        <b>Raw Memory Manipulation</b>
      </a>
    </td>
    <td></td>
  </tr>
</table>

## Architectural Risk Exposures

<table style="width:100%; text-align:center;">
  <tr>
    <td>
      <a href="../assets/analyses_ridgeplots/risk_cognitive_load_exposure_ridgeplot.png">
        <img src="../assets/analyses_ridgeplots/risk_cognitive_load_exposure_ridgeplot.png" width="300" loading="lazy" alt="Cognitive Load Exposure"/><br/>
        <b>Cognitive Load Exposure</b>
      </a>
    </td>
    <td>
      <a href="../assets/analyses_ridgeplots/risk_tech_debt_exposure_ridgeplot.png">
        <img src="../assets/analyses_ridgeplots/risk_tech_debt_exposure_ridgeplot.png" width="300" loading="lazy" alt="Tech Debt Exposure"/><br/>
        <b>Tech Debt Exposure</b>
      </a>
    </td>
    <td>
      <a href="../assets/analyses_ridgeplots/risk_error_and_exception_exposure_ridgeplot.png">
        <img src="../assets/analyses_ridgeplots/risk_error_and_exception_exposure_ridgeplot.png" width="300" loading="lazy" alt="Error & Exception Exposure"/><br/>
        <b>Error & Exception Exposure</b>
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="../assets/analyses_ridgeplots/risk_api_exposure_ridgeplot.png">
        <img src="../assets/analyses_ridgeplots/risk_api_exposure_ridgeplot.png" width="300" loading="lazy" alt="API Exposure"/><br/>
        <b>API Exposure</b>
      </a>
    </td>
    <td>
      <a href="../assets/analyses_ridgeplots/risk_state_flux_exposure_ridgeplot.png">
        <img src="../assets/analyses_ridgeplots/risk_state_flux_exposure_ridgeplot.png" width="300" loading="lazy" alt="State Flux Exposure"/><br/>
        <b>State Flux Exposure</b>
      </a>
    </td>
    <td>
      <a href="../assets/analyses_ridgeplots/risk_concurrency_exposure_ridgeplot.png">
        <img src="../assets/analyses_ridgeplots/risk_concurrency_exposure_ridgeplot.png" width="300" loading="lazy" alt="Concurrency Exposure"/><br/>
        <b>Concurrency Exposure</b>
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="../assets/analyses_ridgeplots/risk_testing_exposure_ridgeplot.png">
        <img src="../assets/analyses_ridgeplots/risk_testing_exposure_ridgeplot.png" width="300" loading="lazy" alt="Testing Exposure"/><br/>
        <b>Testing Exposure</b>
      </a>
    </td>
    <td>
      <a href="../assets/analyses_ridgeplots/risk_documentation_exposure_ridgeplot.png">
        <img src="../assets/analyses_ridgeplots/risk_documentation_exposure_ridgeplot.png" width="300" loading="lazy" alt="Documentation Exposure"/><br/>
        <b>Documentation Exposure</b>
      </a>
    </td>
    <td>
      <a href="../assets/analyses_ridgeplots/risk_specification_exposure_ridgeplot.png">
        <img src="../assets/analyses_ridgeplots/risk_specification_exposure_ridgeplot.png" width="300" loading="lazy" alt="Specification Exposure"/><br/>
        <b>Specification Exposure</b>
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="../assets/analyses_ridgeplots/risk_graveyard_exposure_ridgeplot.png">
        <img src="../assets/analyses_ridgeplots/risk_graveyard_exposure_ridgeplot.png" width="300" loading="lazy" alt="Graveyard Exposure"/><br/>
        <b>Graveyard Exposure</b>
      </a>
    </td>
    <td>
      <a href="../assets/analyses_ridgeplots/risk_civil_war_exposure_ridgeplot.png">
        <img src="../assets/analyses_ridgeplots/risk_civil_war_exposure_ridgeplot.png" width="300" loading="lazy" alt="Civil War (Formatting) Exposure"/><br/>
        <b>Civil War Exposure</b>
      </a>
    </td>
    <td></td>
  </tr>
</table>

## Volatility & Authorship

<table style="width:100%; text-align:center;">
  <tr>
    <td>
      <a href="../assets/analyses_ridgeplots/risk_volatility_exposure_ridgeplot.png">
        <img src="../assets/analyses_ridgeplots/risk_volatility_exposure_ridgeplot.png" width="300" loading="lazy" alt="Volatility Exposure"/><br/>
        <b>Volatility Exposure (Churn)</b>
      </a>
    </td>
    <td>
      <a href="../assets/analyses_ridgeplots/risk_instability_exposure_ridgeplot.png">
        <img src="../assets/analyses_ridgeplots/risk_instability_exposure_ridgeplot.png" width="300" loading="lazy" alt="Instability Exposure"/><br/>
        <b>Instability Exposure (Age)</b>
      </a>
    </td>
    <td>
      <a href="../assets/analyses_ridgeplots/silo_risk_ridgeplot.png">
        <img src="../assets/analyses_ridgeplots/silo_risk_ridgeplot.png" width="300" loading="lazy" alt="Silo Risk"/><br/>
        <b>Silo Risk (Bus Factor)</b>
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="../assets/analyses_ridgeplots/ownership_entropy_ridgeplot.png">
        <img src="../assets/analyses_ridgeplots/ownership_entropy_ridgeplot.png" width="300" loading="lazy" alt="Ownership Entropy"/><br/>
        <b>Ownership Entropy</b>
      </a>
    </td>
    <td></td>
    <td></td>
  </tr>
</table>

## Structural Physics & DNA

<table style="width:100%; text-align:center;">
  <tr>
    <td>
      <a href="../assets/analyses_ridgeplots/structural_mass_ridgeplot.png">
        <img src="../assets/analyses_ridgeplots/structural_mass_ridgeplot.png" width="300" loading="lazy" alt="Structural Mass"/><br/>
        <b>Structural Mass</b>
      </a>
    </td>
    <td>
      <a href="../assets/analyses_ridgeplots/control_flow_ratio_ridgeplot.png">
        <img src="../assets/analyses_ridgeplots/control_flow_ratio_ridgeplot.png" width="300" loading="lazy" alt="Control Flow Ratio"/><br/>
        <b>Control Flow Ratio</b>
      </a>
    </td>
    <td>
      <a href="../assets/analyses_ridgeplots/hit_control_flow_branches_ridgeplot.png">
        <img src="../assets/analyses_ridgeplots/hit_control_flow_branches_ridgeplot.png" width="300" loading="lazy" alt="Control Flow Branches"/><br/>
        <b>Control Flow Branches</b>
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="../assets/analyses_ridgeplots/max_func_complexity_ridgeplot.png">
        <img src="../assets/analyses_ridgeplots/max_func_complexity_ridgeplot.png" width="300" loading="lazy" alt="Max Function Complexity"/><br/>
        <b>Max Function Complexity</b>
      </a>
    </td>
    <td>
      <a href="../assets/analyses_ridgeplots/avg_func_args_ridgeplot.png">
        <img src="../assets/analyses_ridgeplots/avg_func_args_ridgeplot.png" width="300" loading="lazy" alt="Avg Function Arguments"/><br/>
        <b>Avg Function Arguments</b>
      </a>
    </td>
    <td>
      <a href="../assets/analyses_ridgeplots/import_count_ridgeplot.png">
        <img src="../assets/analyses_ridgeplots/import_count_ridgeplot.png" width="300" loading="lazy" alt="Outbound Imports"/><br/>
        <b>Outbound Imports</b>
      </a>
    </td>
  </tr>
  <tr>
    <td>
      <a href="../assets/analyses_ridgeplots/hit_i_o_and_network_boundaries_ridgeplot.png">
        <img src="../assets/analyses_ridgeplots/hit_i_o_and_network_boundaries_ridgeplot.png" width="300" loading="lazy" alt="I/O & Network Boundaries"/><br/>
        <b>I/O & Network Boundaries</b>
      </a>
    </td>
    <td></td>
    <td></td>
  </tr>
</table>
