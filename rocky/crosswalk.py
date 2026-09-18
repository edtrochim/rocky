"""Type crosswalk between the LCCS3 (`xsi:type`) and LChS (`BlockReference`) vocabularies.

Both serialise ISO 19144-2, but the 2023 edition (LChS) renamed and moved a few
things: growth forms are singular (LC_Trees -> LC_Tree), linear surfaces are one
element with a type property, permafrost became a characteristic, and the
cultivated-vegetation sub-characteristics collapsed into one record.

Every mapping carries a note when it loses information, so a table produced
from LCCS3 says what it dropped. Unmapped types are kept under their original
name and flagged; nothing is silently discarded.
"""

from __future__ import annotations

# LCCS3 element xsi:type -> (LChS BlockReference, note)
ELEMENT_LCCS3_TO_LCHS: dict[str, tuple[str, str]] = {
    "LC_Vegetation": ("LC_VegetationElement", ""),
    "LC_GrowthForms": ("LC_GrowthForm", ""),
    "LC_WoodyGrowthForms": ("LC_WoodyGrowthForm", ""),
    "LC_Trees": ("LC_Tree", ""),
    "LC_Shrubs": ("LC_Shrub", ""),
    "LC_HerbaceousGrowthForms": ("LC_HerbaceousGrowthForm", ""),
    "LC_Graminae": ("LC_Graminoid", ""),
    "LC_Forbs": ("LC_Forbs", ""),
    "LC_LichenAndMosses": ("LC_LichenAndMoss", ""),
    "LC_Lichen": ("LC_Lichen", ""),
    "LC_Mosses": ("LC_Moss", ""),
    "LC_Algae": ("LC_Algae", ""),
    "LC_AbioticSurface": ("LC_AbioticElement", ""),
    "LC_ArtificialSurface": ("LC_ArtificialSurfaceElement", ""),
    "LC_BuiltUpSurface": ("LC_BuiltUpSurface", ""),
    "LC_LinearSurface": ("LC_LinearSurface", ""),
    "LC_Road": ("LC_LinearSurface", "LCCS3 LC_Road becomes LC_LinearSurface with linearSurfaceType=Road"),
    "LC_Railway": ("LC_LinearSurface", "LCCS3 LC_Railway becomes LC_LinearSurface with linearSurfaceType=Railway"),
    "LC_CommunicationsAndOther": ("LC_LinearSurface", "LCCS3 LC_CommunicationsAndOther becomes LC_LinearSurface with linearSurfaceType"),
    "LC_NonLinearSurface": ("LC_NonLinearSurface", ""),
    "LC_Building": ("LC_Building", ""),
    "LC_OtherConstruction": ("LC_OtherConstruction", ""),
    "LC_OtherArtificialSurface": ("LC_OtherArtificialSurface", ""),
    "LC_NonBuiltUpSurface": ("LC_NonBuiltUpSurface", ""),
    "LC_DumpSite": ("LC_DumpSite", ""),
    "LC_Deposit": ("LC_NonBuiltUpSurface", "LCCS3 artificial LC_Deposit has no LChS type; kept as non-built-up surface"),
    "LC_Extraction": ("LC_Extraction", ""),
    "LC_NaturalSurface": ("LC_NaturalSurfaceElement", ""),
    "LC_RocksSurface": ("LC_RocksSurfaceElement", ""),
    "LC_BareRocks": ("LC_BareRock", ""),
    "LC_BareRocksAndCoarseFragments": ("LC_BareRock", "LChS splits bare rock and coarse fragments; mapped to LC_BareRock"),
    "LC_HardPans": ("LC_Hardpan", ""),
    "LC_SoilSandDepositSurface": ("LC_SoilSandDepositsSurfaceElement", ""),
    "LC_BareSoil": ("LC_BareSoil", ""),
    "LC_CoarseMineralFragments": ("LC_CoarseMineralFragments", ""),
    "LC_LooseAndShiftingSand": ("LC_LooseAndShiftingSand", ""),
    "LC_Dune": ("LC_Dune", ""),
    "LC_Deposits": ("LC_Deposits", ""),
    "LC_InorganicDeposits": ("LC_InorganicDeposits", ""),
    "LC_OrganicDeposits": ("LC_OrganicDeposits", ""),
    "LC_WaterBodyAndAssociatedSurface": ("LC_WaterBodyAndAssociatedSurfaceElement", ""),
    "LC_WaterBody": ("LC_WaterBody", ""),
    "LC_Snow": ("LC_Snow", ""),
    "LC_Ice": ("LC_Ice", ""),
    "LC_TerrestrialIce": ("LC_TerrestrialIce", ""),
    "LC_FloatingIce": ("LC_FloatingIce", ""),
    "LC_Permafrost": ("LC_WaterBodyAndAssociatedSurfaceElement",
                      "LChS models permafrost as LC_PermafrostCharacteristic on a water/associated element"),
}

# LCCS3 characteristic xsi:type -> (LChS CharacteristicReference, note)
CHAR_LCCS3_TO_LCHS: dict[str, tuple[str, str]] = {
    "LC_WaterSalinity": ("LC_WaterSalinityCharacteristic", ""),
    "LC_WaterChemistry": ("LC_WaterChemistryCharacteristic", ""),
    "LC_Artificiality": ("LC_ArtificialityCharacteristic", ""),
    "LC_Aquaculture": ("LC_AquacultureCharacteristic", ""),
    "LC_ConstructionStatus": ("LC_ConstructionStatusCharacteristic", ""),
    "LC_ConstructionUse": ("LC_ConstructionUse", ""),
    "LC_ArtificialSurfaceCharacteristic": ("LC_ArtificialSurfaceTypes", ""),
    "LC_FloristicAspect": ("LC_FloristicAspectsCharacteristic", ""),
    "LC_FloristicAspectSpecies": ("LC_FloristicAspectsCharacteristic", ""),
    "LC_SinglePlantSpecies": ("LC_FloristicAspectsCharacteristic", ""),
    "LC_GroupOfPlantSpecies": ("LC_FloristicAspectsCharacteristic", ""),
    "LC_AllometricMeasurements": ("LC_AllometricMeasurementsCharacteristic", ""),
    "LC_GrowthFormAge": ("LC_GrowthFormAgeCharacteristic", ""),
    "LC_EvenAge": ("LC_GrowthFormAgeCharacteristic", ""),
    "LC_UnevenAge": ("LC_GrowthFormAgeCharacteristic", ""),
    "LC_BurntStatus": ("LC_BurntStatusCharacteristic", ""),
    "LC_DeadStatus": ("LC_DeadStatusCharacteristic", ""),
    "LC_VegetationDamage": ("LC_VegetationDamageCharacteristic", ""),
    "LC_WaterStress": ("LC_WaterStressCharacteristic", ""),
    "LC_GrowthFormIllness": ("LC_GrowthFormIllnessCharacteristic", ""),
    "LC_Grazing": ("LC_GrazedCharacteristic", ""),
    "LC_GrazingAnimalType": ("LC_GrazedCharacteristic", ""),
    "LC_NaturalOrSeminaturalVegetation": ("LC_VegetationArtificialityCharacteristic", "value: Natural or Seminatural"),
    "LC_CultivatedAndManagedVegetation": ("LC_CultivatedAndManagedVegetationCharacteristics", ""),
    "LC_UrbanPark": ("LC_CultivatedAndManagedVegetationCharacteristics", "LCCS3 urban park"),
    "LC_CropYield": ("LC_CultivatedAndManagedVegetationCharacteristics", ""),
    "LC_Plantation": ("LC_CultivatedAndManagedVegetationCharacteristics", ""),
    "LC_ForestPlantation": ("LC_CultivatedAndManagedVegetationCharacteristics", "treePlantation"),
    "LC_OrchardAndOtherPlantation": ("LC_CultivatedAndManagedVegetationCharacteristics", "orchardAndOtherPlantation"),
    "LC_CropGrowingParameter": ("LC_CultivatedAndManagedVegetationCharacteristics", ""),
    "LC_OverlapGrowingToReferenceCrop": ("LC_CultivatedAndManagedVegetationCharacteristics", ""),
    "LC_CropRotation": ("LC_CultivatedAndManagedVegetationCharacteristics", ""),
    "LC_PlantSpreadingGeometry": ("LC_CultivatedAndManagedVegetationCharacteristics", ""),
    "LC_FieldDistribution": ("LC_CultivatedAndManagedVegetationCharacteristics", ""),
    "LC_Irrigation": ("LC_CultivatedAndManagedVegetationCharacteristics", "irrigationType"),
    "LC_Postflooding": ("LC_CultivatedAndManagedVegetationCharacteristics", "postfloodingPercentage"),
    "LC_Rainfed": ("LC_CultivatedAndManagedVegetationCharacteristics", "rainfedPercentage"),
    "LC_FieldSize": ("LC_CultivatedAndManagedVegetationCharacteristics", "fieldSize"),
    "LC_MechanicalErosionControl": ("LC_CultivatedAndManagedVegetationCharacteristics", "mechanicalErosionControl"),
    "LC_PestControl": ("LC_CultivatedAndManagedVegetationCharacteristics", "land-use practice in ISO 19144-3"),
    "LC_CropFertilization": ("LC_CultivatedAndManagedVegetationCharacteristics", "land-use practice in ISO 19144-3"),
    "LC_Ploughing": ("LC_CultivatedAndManagedVegetationCharacteristics", "ploughType"),
    "LC_TreeAreaManagementPractices": ("LC_CultivatedAndManagedVegetationCharacteristics", "land-use practice in ISO 19144-3"),
    "LC_MultiTreeAreaManagementPractices": ("LC_CultivatedAndManagedVegetationCharacteristics", "not in either schema"),
    "LC_MultiTreeAreaManagementPractice": ("LC_CultivatedAndManagedVegetationCharacteristics", "not in either schema"),
    "LC_Permafrost": ("LC_PermafrostCharacteristic", ""),
    "LC_ArtificialSurfaceDamage": ("LC_ArtificialSurfaceDamageCharacteristic", ""),
}

# LChS BlockReference -> preferred LCCS3 xsi:type (first exact match wins)
ELEMENT_LCHS_TO_LCCS3: dict[str, str] = {}
for _k, (_v, _n) in ELEMENT_LCCS3_TO_LCHS.items():
    if _n == "" and _v not in ELEMENT_LCHS_TO_LCCS3:
        ELEMENT_LCHS_TO_LCCS3[_v] = _k

CHAR_LCHS_TO_LCCS3: dict[str, str] = {}
for _k, (_v, _n) in CHAR_LCCS3_TO_LCHS.items():
    if _n == "" and _v not in CHAR_LCHS_TO_LCCS3:
        CHAR_LCHS_TO_LCCS3[_v] = _k

# LChS BlockID / CharacteristicID type codes as FAO's tool writes them (from registry files).
# Unknown refs get an ordinal; the codes are what the LChS desktop tool expects.
LCHS_BLOCK_CODES = {
    "LC_GrowthForm": "1003", "LC_WoodyGrowthForm": "1004", "LC_Tree": "1005", "LC_Shrub": "1006",
    "LC_HerbaceousGrowthForm": "1007", "LC_ArtificialSurfaceElement": "1014", "LC_BuiltUpSurface": "1018",
    "LC_NaturalSurfaceElement": "1024", "LC_BareSoil": "1029", "LC_WaterBody": "1037",
}
LCHS_CHAR_CODES = {
    "LC_WaterSalinityCharacteristic": "100001", "LC_ArtificialityCharacteristic": "100003",
    "LC_VegetationArtificialityCharacteristic": "100020",
    "LC_CultivatedAndManagedVegetationCharacteristics": "100021",
}

# LCCS3 presence values <-> LChS
PRESENCE_LCCS3_TO_LCHS = {"Mandatory": "Fixed", "Optional": "Conditional Temporal",
                          "Exclusive": "Exclusive", "Temporal Sequence Depending": "Conditional Temporal"}
PRESENCE_LCHS_TO_LCCS3 = {"Fixed": "Mandatory", "fixed": "Mandatory", "Mandatory": "Mandatory",
                          "Conditional Temporal": "Optional", "conditionalTemporal": "Optional",
                          "Optional": "Optional", "Exclusive": "Exclusive", "exclusive": "Exclusive",
                          "Precluded": "Optional", "precluded": "Optional"}


def element_to_lchs(lccs3_type: str) -> tuple[str, str]:
    return ELEMENT_LCCS3_TO_LCHS.get(lccs3_type, (lccs3_type, "no LChS equivalent; kept as-is"))


def char_to_lchs(lccs3_type: str) -> tuple[str, str]:
    return CHAR_LCCS3_TO_LCHS.get(lccs3_type, (lccs3_type, "no LChS equivalent; kept as-is"))


def element_to_lccs3(lchs_ref: str) -> str | None:
    return ELEMENT_LCHS_TO_LCCS3.get(lchs_ref)


def char_to_lccs3(lchs_ref: str) -> str | None:
    return CHAR_LCHS_TO_LCCS3.get(lchs_ref)
