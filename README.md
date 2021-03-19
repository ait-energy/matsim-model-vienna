# MATSim Model Vienna: Open Access

This repository contains data for a traffic simulation for the city and agglomeration of Vienna
with [MATSim](https://matsim.org) - the **M**ulti-**A**gent **T**ransport **Sim**ulation.

> Note, that the **open access model** is a **reduced version of the full model available at [AIT](http://www.ait.ac.at)**,
> with intermodal routing of the agents' trips being the most important advantage of the full model.
> The open access model is provided in the spirit of open scientific research
> and is not ready for precise traffic planning activities (contrary to the full model).


## Run the Model

To run the simulation:

1. Download or clone this repository
2. Download [the full population (password: matsim12)](https://nextcloud.ait.ac.at/index.php/s/T3K2ybHd5QxpR2e) and put it into the folder created in the previous step
   - It is too large for hosting on GitHub
3. Optionally change the population in the config:
   - Default is the full population (12.5% of the mobile population)
   - For a quick test you can use the small population containing 500 randomly selected agents of the full population
4. Download the [MATSim 12.0 release](https://matsim.org/downloads)
5. Run the MATSim GUI
   - Select the configuration file
   - Set `Memory` to 4 GB for the full population (or 2 GB for the small population)
   - Start the simulation

> Note: 500 agents is also the maximum number of agents to visualize the results in [Simunto Via](https://simunto.com/via/) with a free license.


## The Model in a Nutshell

- **Simulation Area:** Vienna and surroundings in a 30km radius (total population: 2.33 million, area: 4170 km²)
- **Network**: 156k links and 71k nodes extracted from [OpenStreetMap](https://www.openstreetmap.org) with [pt2matsim](https://github.com/matsim-org/pt2matsim)
- **Facilities:** 435k locations extracted from [OpenStreetMap](https://www.openstreetmap.org) and the [geostat population density grid (2011)](https://ec.europa.eu/eurostat/de/web/gisco/geodata/reference-data/population-distribution-demography/geostat)
- **Population synthesis**: based on the Austrian mobility survey *Österreich Unterwegs 2013/14*
- **Population**: 200k agents represent 12.5% of the mobile population older than 17 years. The agents use the MATSim modes walk, bike, pt, car.
- **Routing**:
  - open access model: MATSim car routing and teleporting for all other modes
  - full model: *Ariadne* intermodal routing framework calculating exact travel times for all modes and also allowing for intermodal trips such as park and ride
- **Mode choice model:** based on travel survey from WU/BOKU Vienna; 10 subpopulations with different utility functions. Assignment of an agent to a subpopulation depends on socio-economic characteristics, see below for further details
- **Calibration:** 180 count stations for traffic volumes, normalized error for peak hours:
  - open access model: 0.4
  - full model: 0.33

![Area covered by the MATSim Model Vienna](matsim_model_vienna_area.jpg)

Area covered by the MATSim Model Vienna, light-blue areas contain facilities.

## Highlights

The model's highlights are **intermodal routing** and **different values of travel time for subpopulations**.

### Intermodal Routing

The MATSim Model Vienna is intermodal through usage of the *Ariadne* routing framework,
i.e. **allows for park and ride or combining cycling with demand responsive transport on a single leg**.

In the full model we follow the same approach as described by Hörl et al (2019),
where the classic MATSim cycle of trial and error with random changes to plans
is discarded as it would take too much time to fully explore all intermodal possibilities.
This leads to much **faster convergence towards a state of equilibrium**.

Instead of random changes to the agents' plans we use *Ariadne* to **only generate plausible intermodal plans**.
To further increase the simulation time all plausible plans are pre-calculated and cached for the whole population.
This cache can then be used for all simulation runs.


### Subpopulations & Value of Travel Time

The model features **different values of travel time** for the simulated agents which are represented in the parameters of the Charypar-Nagel function.
These do not depend - as mostly done - on the home location of the agent but on **socio-demographic characteristics assigned to the agents**.

The mode choice parameters are estimated for two (latent) classes by SP-off-RP surveys together with probabilities indicating that persons with particular characteristics are part of each class (Greene and Hensher, 2003).
Depending on the socio-demographics of each agent, we yield the probability of him/her to be part of each of the two classes.
Based on these probabilities, we split the population in ten supopulations (according to quantiles), and estimate the parameters for each subpopulation.

This highlight is also available in the open access model (see the subpopulations in [config.xml](config.xml))!


## Differences Between the Open Access Model and the Full Model

While the **full model is intermodal** through usage of the *Ariadne* routing framework,
the **open access model only uses MATSim car routing and teleportation of all other modes**.

The open access model

1. is coarsely calibrated (+/-4% difference to the actual modal split).
2. tends to underestimate trip durations and distances by around  30% due to teleporting instead of actual route calculation all modes but car.


## Literature

- Hörl, S., Balać, M., & Axhausen, K. W. (2019). *Pairing discrete mode choice models and agent-based transport simulation with MATSim*. In 2019 TRB Annual Meeting Online (pp. 19-02409).
- Greene, W. H., & Hensher, D. A. (2003). *A latent class model for discrete choice analysis: contrasts with mixed logit*. Transportation Research Part B: Methodological, 37(8), 681-698.

### Preferred Citation

If you use the MATSim Model Vienna and write a scientific paper about it, please cite the following paper as a reference.

- Müller, J., Straub, M., Naqvi, A.,  Richter, G., Peer, S., & Rudloff, C. (2021). *MATSim Model Vienna: Analyzing the Socioeconomic Impacts for Different Fleet Sizes and Pricing Schemes of Shared Autonomous Electric Vehicles*. Proceedings of the 100th Annual Meeting of the Transportation Research Board. Available on [ResearchGate](https://www.researchgate.net/publication/349212535_MATSim_Model_Vienna_Analyzing_the_Socioeconomic_Impacts_for_Different_Fleet_Sizes_and_Pricing_Schemes_of_Shared_Autonomous_Electric_Vehicles).

## License

The open access MATSim Model Vienna is published under license [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0).
You may use it for all non-commercial activities, and must give appropriate credit, provide a link to the license, and indicate if changes were made.
