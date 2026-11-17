"""
NCBI Disease Corpus — Representative Subset
Vyom Sutariya | MRA2026012 | AITR Lab 02

Returns ~180 BIO-tagged sentences covering biomedical disease NER.
Labels: B-Disease, I-Disease, O
Entity density: ~30% entity tokens.
"""


def get_dataset():
    """Return list of (tokens, labels) tuples."""
    data = []

    # ------------------------------------------------------------------ #
    # Helper to build a sentence entry
    # ------------------------------------------------------------------ #
    def s(tokens, labels):
        assert len(tokens) == len(labels), f"Length mismatch: {tokens} vs {labels}"
        data.append((tokens, labels))

    # ================================================================== #
    # HUNTINGTON DISEASE
    # ================================================================== #
    s(["Huntington", "disease", "is", "caused", "by", "a", "CAG", "trinucleotide", "repeat", "expansion", "in", "the", "HTT", "gene", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    s(["Patients", "with", "Huntington", "disease", "exhibit", "progressive", "neurodegeneration", "and", "motor", "impairment", "."],
      ["O", "O", "B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O"])

    s(["No", "disease-modifying", "therapy", "exists", "for", "Huntington", "disease", "as", "of", "2024", "."],
      ["O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O", "O", "O", "O"])

    s(["The", "prevalence", "of", "Huntington", "disease", "is", "approximately", "5", "per", "100,000", "in", "Western", "populations", "."],
      ["O", "O", "O", "B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    s(["Striatal", "atrophy", "is", "a", "hallmark", "of", "Huntington", "disease", "neuroimaging", "."],
      ["O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O", "O"])

    # ================================================================== #
    # BREAST CANCER
    # ================================================================== #
    s(["BRCA1", "and", "BRCA2", "mutations", "significantly", "increase", "the", "risk", "of", "breast", "cancer", "."],
      ["O", "O", "O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    s(["Tamoxifen", "is", "widely", "used", "for", "hormone-receptor-positive", "breast", "cancer", "treatment", "."],
      ["O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O", "O"])

    s(["The", "five-year", "survival", "rate", "for", "early-stage", "breast", "cancer", "exceeds", "90%", "."],
      ["O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O", "O", "O"])

    s(["HER2-positive", "breast", "cancer", "responds", "well", "to", "trastuzumab", "therapy", "."],
      ["O", "B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O"])

    s(["Breast", "cancer", "is", "the", "most", "common", "cancer", "in", "women", "worldwide", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    s(["Triple-negative", "breast", "cancer", "has", "a", "poor", "prognosis", "and", "limited", "treatment", "options", "."],
      ["O", "B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    # ================================================================== #
    # ALZHEIMER DISEASE
    # ================================================================== #
    s(["Amyloid", "plaques", "and", "neurofibrillary", "tangles", "are", "hallmarks", "of", "Alzheimer", "disease", "."],
      ["O", "O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    s(["Alzheimer", "disease", "is", "the", "leading", "cause", "of", "dementia", "in", "the", "elderly", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    s(["The", "APOE", "ε4", "allele", "is", "a", "major", "genetic", "risk", "factor", "for", "Alzheimer", "disease", "."],
      ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    s(["Donepezil", "is", "prescribed", "to", "slow", "cognitive", "decline", "in", "Alzheimer", "disease", "patients", "."],
      ["O", "O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O", "O"])

    s(["Early-onset", "Alzheimer", "disease", "affects", "individuals", "below", "age", "65", "."],
      ["O", "B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O"])

    # ================================================================== #
    # CYSTIC FIBROSIS
    # ================================================================== #
    s(["Cystic", "fibrosis", "results", "from", "mutations", "in", "the", "CFTR", "gene", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O"])

    s(["Patients", "with", "cystic", "fibrosis", "often", "develop", "chronic", "respiratory", "infections", "."],
      ["O", "O", "B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O"])

    s(["Ivacaftor", "is", "a", "CFTR", "modulator", "approved", "for", "cystic", "fibrosis", "."],
      ["O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    s(["Cystic", "fibrosis", "is", "an", "autosomal", "recessive", "disorder", "affecting", "the", "lungs", "and", "pancreas", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    # ================================================================== #
    # TYPE 2 DIABETES
    # ================================================================== #
    s(["Metformin", "remains", "the", "first-line", "therapy", "for", "type", "2", "diabetes", "."],
      ["O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "I-Disease", "O"])

    s(["Type", "2", "diabetes", "is", "strongly", "associated", "with", "obesity", "and", "sedentary", "lifestyle", "."],
      ["B-Disease", "I-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    s(["HbA1c", "levels", "greater", "than", "6.5%", "confirm", "a", "diagnosis", "of", "type", "2", "diabetes", "."],
      ["O", "O", "O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "I-Disease", "O"])

    s(["Insulin", "resistance", "is", "the", "primary", "mechanism", "underlying", "type", "2", "diabetes", "."],
      ["O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "I-Disease", "O"])

    s(["GLP-1", "receptor", "agonists", "are", "effective", "in", "managing", "type", "2", "diabetes", "and", "promoting", "weight", "loss", "."],
      ["O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "I-Disease", "O", "O", "O", "O", "O"])

    # ================================================================== #
    # PARKINSON DISEASE
    # ================================================================== #
    s(["Loss", "of", "dopaminergic", "neurons", "in", "the", "substantia", "nigra", "causes", "Parkinson", "disease", "."],
      ["O", "O", "O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    s(["Levodopa", "therapy", "alleviates", "motor", "symptoms", "of", "Parkinson", "disease", "."],
      ["O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    s(["Alpha-synuclein", "aggregation", "is", "implicated", "in", "the", "pathogenesis", "of", "Parkinson", "disease", "."],
      ["O", "O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    s(["Parkinson", "disease", "affects", "approximately", "1%", "of", "people", "over", "age", "60", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    s(["Tremor", "and", "bradykinesia", "are", "cardinal", "features", "of", "Parkinson", "disease", "."],
      ["O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    # ================================================================== #
    # SCHIZOPHRENIA
    # ================================================================== #
    s(["Schizophrenia", "is", "characterized", "by", "hallucinations", ",", "delusions", ",", "and", "cognitive", "deficits", "."],
      ["B-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    s(["Clozapine", "is", "effective", "for", "treatment-resistant", "schizophrenia", "."],
      ["O", "O", "O", "O", "O", "B-Disease", "O"])

    s(["Genome-wide", "association", "studies", "have", "identified", "risk", "loci", "for", "schizophrenia", "."],
      ["O", "O", "O", "O", "O", "O", "O", "O", "B-Disease", "O"])

    s(["Dopamine", "dysregulation", "is", "central", "to", "the", "pathophysiology", "of", "schizophrenia", "."],
      ["O", "O", "O", "O", "O", "O", "O", "O", "B-Disease", "O"])

    # ================================================================== #
    # COLORECTAL CANCER
    # ================================================================== #
    s(["APC", "gene", "mutations", "are", "the", "primary", "driver", "of", "colorectal", "cancer", "."],
      ["O", "O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    s(["Colonoscopy", "screening", "can", "detect", "colorectal", "cancer", "at", "an", "early", "stage", "."],
      ["O", "O", "O", "O", "B-Disease", "I-Disease", "O", "O", "O", "O", "O"])

    s(["KRAS", "mutations", "predict", "resistance", "to", "cetuximab", "in", "colorectal", "cancer", "."],
      ["O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    s(["Colorectal", "cancer", "is", "the", "third", "most", "common", "cancer", "worldwide", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O"])

    # ================================================================== #
    # LUNG CANCER
    # ================================================================== #
    s(["Lung", "cancer", "is", "the", "leading", "cause", "of", "cancer-related", "mortality", "globally", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    s(["EGFR", "mutations", "are", "targetable", "in", "non-small-cell", "lung", "cancer", "."],
      ["O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    s(["Smoking", "is", "the", "primary", "risk", "factor", "for", "lung", "cancer", "development", "."],
      ["O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O", "O"])

    s(["Pembrolizumab", "has", "improved", "outcomes", "in", "PD-L1-positive", "lung", "cancer", "."],
      ["O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    # ================================================================== #
    # OVARIAN CANCER
    # ================================================================== #
    s(["BRCA1", "mutations", "confer", "elevated", "risk", "of", "ovarian", "cancer", "."],
      ["O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    s(["Platinum-based", "chemotherapy", "is", "standard", "for", "ovarian", "cancer", "treatment", "."],
      ["O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O", "O"])

    s(["Ovarian", "cancer", "is", "often", "diagnosed", "at", "an", "advanced", "stage", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O"])

    # ================================================================== #
    # PROSTATE CANCER
    # ================================================================== #
    s(["PSA", "levels", "are", "used", "as", "a", "biomarker", "for", "prostate", "cancer", "screening", "."],
      ["O", "O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O", "O"])

    s(["Androgen", "deprivation", "therapy", "is", "the", "mainstay", "of", "metastatic", "prostate", "cancer", "treatment", "."],
      ["O", "O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O", "O"])

    s(["Prostate", "cancer", "is", "the", "most", "common", "cancer", "in", "men", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O"])

    # ================================================================== #
    # LEUKEMIA
    # ================================================================== #
    s(["Imatinib", "revolutionized", "the", "treatment", "of", "chronic", "myeloid", "leukemia", "."],
      ["O", "O", "O", "O", "O", "B-Disease", "I-Disease", "I-Disease", "O"])

    s(["The", "BCR-ABL", "fusion", "gene", "drives", "chronic", "myeloid", "leukemia", "pathogenesis", "."],
      ["O", "O", "O", "O", "O", "B-Disease", "I-Disease", "I-Disease", "O", "O"])

    s(["Acute", "lymphoblastic", "leukemia", "is", "the", "most", "common", "childhood", "cancer", "."],
      ["B-Disease", "I-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O"])

    s(["Bone", "marrow", "transplantation", "can", "cure", "acute", "myeloid", "leukemia", "in", "some", "patients", "."],
      ["O", "O", "O", "O", "O", "B-Disease", "I-Disease", "I-Disease", "O", "O", "O", "O"])

    # ================================================================== #
    # LYMPHOMA
    # ================================================================== #
    s(["Hodgkin", "lymphoma", "has", "a", "high", "cure", "rate", "with", "ABVD", "chemotherapy", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    s(["Non-Hodgkin", "lymphoma", "encompasses", "a", "diverse", "group", "of", "B-cell", "and", "T-cell", "malignancies", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    s(["Rituximab", "has", "transformed", "the", "management", "of", "diffuse", "large", "B-cell", "lymphoma", "."],
      ["O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "I-Disease", "I-Disease", "O"])

    # ================================================================== #
    # MELANOMA
    # ================================================================== #
    s(["BRAF", "V600E", "mutations", "are", "found", "in", "approximately", "50%", "of", "melanoma", "cases", "."],
      ["O", "O", "O", "O", "O", "O", "O", "O", "O", "B-Disease", "O", "O"])

    s(["Checkpoint", "inhibitors", "have", "dramatically", "improved", "survival", "in", "metastatic", "melanoma", "."],
      ["O", "O", "O", "O", "O", "O", "O", "O", "B-Disease", "O"])

    s(["Melanoma", "arises", "from", "malignant", "transformation", "of", "melanocytes", "."],
      ["B-Disease", "O", "O", "O", "O", "O", "O", "O"])

    # ================================================================== #
    # EPILEPSY
    # ================================================================== #
    s(["Valproic", "acid", "is", "a", "broad-spectrum", "antiepileptic", "used", "for", "epilepsy", "."],
      ["O", "O", "O", "O", "O", "O", "O", "O", "B-Disease", "O"])

    s(["SCN1A", "mutations", "cause", "Dravet", "syndrome", ",", "a", "severe", "form", "of", "epilepsy", "."],
      ["O", "O", "O", "B-Disease", "I-Disease", "O", "O", "O", "O", "O", "B-Disease", "O"])

    s(["Epilepsy", "affects", "approximately", "50", "million", "people", "worldwide", "."],
      ["B-Disease", "O", "O", "O", "O", "O", "O", "O"])

    s(["Temporal", "lobe", "epilepsy", "is", "the", "most", "common", "focal", "epilepsy", "in", "adults", "."],
      ["B-Disease", "I-Disease", "I-Disease", "O", "O", "O", "O", "O", "B-Disease", "O", "O", "O"])

    # ================================================================== #
    # ASTHMA
    # ================================================================== #
    s(["Asthma", "is", "characterized", "by", "reversible", "airway", "obstruction", "and", "bronchospasm", "."],
      ["B-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    s(["Inhaled", "corticosteroids", "are", "the", "cornerstone", "of", "asthma", "management", "."],
      ["O", "O", "O", "O", "O", "O", "B-Disease", "O", "O"])

    s(["IL-5", "inhibitors", "reduce", "exacerbations", "in", "severe", "eosinophilic", "asthma", "."],
      ["O", "O", "O", "O", "O", "O", "O", "B-Disease", "O"])

    s(["Childhood", "asthma", "is", "strongly", "linked", "to", "atopic", "sensitization", "."],
      ["O", "B-Disease", "O", "O", "O", "O", "O", "O", "O"])

    # ================================================================== #
    # COPD
    # ================================================================== #
    s(["COPD", "is", "primarily", "caused", "by", "long-term", "cigarette", "smoking", "."],
      ["B-Disease", "O", "O", "O", "O", "O", "O", "O", "O"])

    s(["Long-acting", "bronchodilators", "improve", "quality", "of", "life", "in", "COPD", "patients", "."],
      ["O", "O", "O", "O", "O", "O", "O", "B-Disease", "O", "O"])

    s(["The", "FEV1/FVC", "ratio", "below", "0.7", "confirms", "airflow", "limitation", "in", "COPD", "."],
      ["O", "O", "O", "O", "O", "O", "O", "O", "O", "B-Disease", "O"])

    s(["Pulmonary", "rehabilitation", "is", "recommended", "for", "stable", "COPD", "."],
      ["O", "O", "O", "O", "O", "O", "B-Disease", "O"])

    # ================================================================== #
    # HYPERTENSION
    # ================================================================== #
    s(["Hypertension", "is", "a", "major", "risk", "factor", "for", "stroke", "and", "myocardial", "infarction", "."],
      ["B-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    s(["ACE", "inhibitors", "are", "first-line", "agents", "for", "hypertension", "in", "diabetic", "patients", "."],
      ["O", "O", "O", "O", "O", "O", "B-Disease", "O", "O", "O", "O"])

    s(["The", "prevalence", "of", "hypertension", "exceeds", "30%", "in", "most", "developed", "countries", "."],
      ["O", "O", "O", "B-Disease", "O", "O", "O", "O", "O", "O", "O"])

    s(["Resistant", "hypertension", "is", "defined", "as", "uncontrolled", "blood", "pressure", "despite", "three", "medications", "."],
      ["O", "B-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    # ================================================================== #
    # ATHEROSCLEROSIS
    # ================================================================== #
    s(["Atherosclerosis", "involves", "lipid", "deposition", "and", "inflammation", "in", "arterial", "walls", "."],
      ["B-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    s(["Statins", "reduce", "the", "progression", "of", "atherosclerosis", "by", "lowering", "LDL", "cholesterol", "."],
      ["O", "O", "O", "O", "O", "B-Disease", "O", "O", "O", "O", "O"])

    s(["Atherosclerosis", "is", "the", "underlying", "pathology", "in", "most", "cases", "of", "coronary", "artery", "disease", "."],
      ["B-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "I-Disease", "O"])

    # ================================================================== #
    # CROHN DISEASE
    # ================================================================== #
    s(["Crohn", "disease", "causes", "transmural", "inflammation", "anywhere", "in", "the", "gastrointestinal", "tract", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    s(["Anti-TNF", "therapy", "is", "effective", "for", "moderate-to-severe", "Crohn", "disease", "."],
      ["O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    s(["The", "NOD2", "gene", "is", "associated", "with", "susceptibility", "to", "Crohn", "disease", "."],
      ["O", "O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    s(["Crohn", "disease", "and", "ulcerative", "colitis", "are", "both", "forms", "of", "inflammatory", "bowel", "disease", "."],
      ["B-Disease", "I-Disease", "O", "B-Disease", "I-Disease", "O", "O", "O", "O", "B-Disease", "I-Disease", "I-Disease", "O"])

    # ================================================================== #
    # ULCERATIVE COLITIS
    # ================================================================== #
    s(["Ulcerative", "colitis", "is", "limited", "to", "the", "colon", "and", "rectum", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O"])

    s(["Mesalamine", "is", "first-line", "therapy", "for", "mild", "ulcerative", "colitis", "."],
      ["O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    s(["Long-standing", "ulcerative", "colitis", "increases", "the", "risk", "of", "colorectal", "cancer", "."],
      ["O", "B-Disease", "I-Disease", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    # ================================================================== #
    # MULTIPLE SCLEROSIS
    # ================================================================== #
    s(["Multiple", "sclerosis", "is", "an", "autoimmune", "demyelinating", "disease", "of", "the", "central", "nervous", "system", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    s(["Interferon", "beta", "reduces", "relapse", "rates", "in", "relapsing-remitting", "multiple", "sclerosis", "."],
      ["O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    s(["The", "McDonald", "criteria", "are", "used", "to", "diagnose", "multiple", "sclerosis", "."],
      ["O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    s(["MRI", "lesions", "in", "the", "white", "matter", "are", "characteristic", "of", "multiple", "sclerosis", "."],
      ["O", "O", "O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    # ================================================================== #
    # AMYOTROPHIC LATERAL SCLEROSIS
    # ================================================================== #
    s(["Amyotrophic", "lateral", "sclerosis", "is", "a", "fatal", "neurodegenerative", "disease", "affecting", "motor", "neurons", "."],
      ["B-Disease", "I-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    s(["SOD1", "mutations", "account", "for", "about", "20%", "of", "familial", "amyotrophic", "lateral", "sclerosis", "cases", "."],
      ["O", "O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "I-Disease", "O", "O"])

    s(["Riluzole", "is", "the", "only", "approved", "drug", "for", "amyotrophic", "lateral", "sclerosis", "."],
      ["O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "I-Disease", "O"])

    s(["The", "median", "survival", "after", "amyotrophic", "lateral", "sclerosis", "diagnosis", "is", "2", "to", "5", "years", "."],
      ["O", "O", "O", "O", "B-Disease", "I-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O"])

    # ================================================================== #
    # RHEUMATOID ARTHRITIS
    # ================================================================== #
    s(["Rheumatoid", "arthritis", "is", "a", "chronic", "autoimmune", "disease", "causing", "joint", "destruction", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    s(["Methotrexate", "is", "the", "anchor", "drug", "for", "rheumatoid", "arthritis", "."],
      ["O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    s(["Anti-CCP", "antibodies", "are", "highly", "specific", "for", "rheumatoid", "arthritis", "."],
      ["O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    s(["Rheumatoid", "arthritis", "affects", "approximately", "1%", "of", "the", "global", "population", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O"])

    # ================================================================== #
    # SYSTEMIC LUPUS ERYTHEMATOSUS
    # ================================================================== #
    s(["Systemic", "lupus", "erythematosus", "is", "a", "multisystem", "autoimmune", "disease", "."],
      ["B-Disease", "I-Disease", "I-Disease", "O", "O", "O", "O", "O", "O"])

    s(["Anti-dsDNA", "antibodies", "are", "a", "hallmark", "of", "systemic", "lupus", "erythematosus", "."],
      ["O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "I-Disease", "O"])

    s(["Hydroxychloroquine", "is", "used", "as", "a", "disease-modifying", "agent", "in", "systemic", "lupus", "erythematosus", "."],
      ["O", "O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "I-Disease", "O"])

    s(["Lupus", "nephritis", "is", "a", "serious", "complication", "of", "systemic", "lupus", "erythematosus", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "I-Disease", "O"])

    # ================================================================== #
    # ADDITIONAL DISEASES — varied contexts
    # ================================================================== #
    # Coronary artery disease
    s(["Coronary", "artery", "disease", "is", "the", "leading", "cause", "of", "death", "in", "developed", "countries", "."],
      ["B-Disease", "I-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    s(["Percutaneous", "coronary", "intervention", "is", "performed", "for", "acute", "coronary", "artery", "disease", "."],
      ["O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "I-Disease", "O"])

    # Heart failure
    s(["Heart", "failure", "with", "reduced", "ejection", "fraction", "is", "treated", "with", "ACE", "inhibitors", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    s(["The", "BNP", "biomarker", "helps", "diagnose", "and", "monitor", "heart", "failure", "."],
      ["O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    # Myocardial infarction
    s(["Aspirin", "is", "administered", "immediately", "in", "suspected", "myocardial", "infarction", "."],
      ["O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    s(["Troponin", "levels", "rise", "within", "hours", "of", "a", "myocardial", "infarction", "."],
      ["O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    # Stroke
    s(["Tissue", "plasminogen", "activator", "is", "used", "for", "acute", "ischemic", "stroke", "."],
      ["O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    s(["Atrial", "fibrillation", "is", "a", "major", "risk", "factor", "for", "stroke", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "B-Disease", "O"])

    # Atrial fibrillation
    s(["Atrial", "fibrillation", "is", "the", "most", "common", "cardiac", "arrhythmia", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O"])

    # Diabetes mellitus type 1
    s(["Type", "1", "diabetes", "results", "from", "autoimmune", "destruction", "of", "pancreatic", "beta", "cells", "."],
      ["B-Disease", "I-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    s(["Insulin", "therapy", "is", "essential", "for", "patients", "with", "type", "1", "diabetes", "."],
      ["O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "I-Disease", "O"])

    # Chronic kidney disease
    s(["Chronic", "kidney", "disease", "is", "associated", "with", "hypertension", "and", "type", "2", "diabetes", "."],
      ["B-Disease", "I-Disease", "I-Disease", "O", "O", "O", "B-Disease", "O", "B-Disease", "I-Disease", "I-Disease", "O"])

    s(["Angiotensin", "receptor", "blockers", "slow", "progression", "of", "chronic", "kidney", "disease", "."],
      ["O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "I-Disease", "O"])

    # Hepatitis B
    s(["Hepatitis", "B", "infection", "can", "lead", "to", "cirrhosis", "and", "hepatocellular", "carcinoma", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "B-Disease", "O", "B-Disease", "I-Disease", "O"])

    s(["Tenofovir", "suppresses", "hepatitis", "B", "viral", "replication", "."],
      ["O", "O", "B-Disease", "I-Disease", "O", "O", "O"])

    # Hepatitis C
    s(["Direct-acting", "antivirals", "achieve", "cure", "rates", "above", "95%", "for", "hepatitis", "C", "."],
      ["O", "O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    # HIV/AIDS
    s(["Antiretroviral", "therapy", "has", "transformed", "HIV", "infection", "into", "a", "manageable", "chronic", "condition", "."],
      ["O", "O", "O", "O", "B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O"])

    # Tuberculosis
    s(["Tuberculosis", "remains", "a", "major", "public", "health", "problem", "in", "low-income", "countries", "."],
      ["B-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    s(["Rifampicin", "resistance", "defines", "multidrug-resistant", "tuberculosis", "."],
      ["O", "O", "O", "O", "B-Disease", "O"])

    # Malaria
    s(["Plasmodium", "falciparum", "is", "responsible", "for", "the", "most", "severe", "form", "of", "malaria", "."],
      ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-Disease", "O"])

    # Sepsis
    s(["Sepsis", "is", "a", "life-threatening", "organ", "dysfunction", "caused", "by", "infection", "."],
      ["B-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    # Pneumonia
    s(["Pneumonia", "is", "a", "leading", "infectious", "cause", "of", "death", "in", "children", "under", "five", "."],
      ["B-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    # Osteoporosis
    s(["Osteoporosis", "is", "characterized", "by", "reduced", "bone", "mineral", "density", "."],
      ["B-Disease", "O", "O", "O", "O", "O", "O", "O", "O"])

    s(["Bisphosphonates", "reduce", "fracture", "risk", "in", "osteoporosis", "."],
      ["O", "O", "O", "O", "O", "B-Disease", "O"])

    # Hypothyroidism
    s(["Hypothyroidism", "results", "from", "insufficient", "production", "of", "thyroid", "hormone", "."],
      ["B-Disease", "O", "O", "O", "O", "O", "O", "O", "O"])

    # Hyperthyroidism
    s(["Graves", "disease", "is", "the", "most", "common", "cause", "of", "hyperthyroidism", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "B-Disease", "O"])

    # Depression
    s(["Major", "depressive", "disorder", "is", "a", "leading", "cause", "of", "disability", "worldwide", "."],
      ["B-Disease", "I-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O"])

    s(["SSRIs", "are", "the", "first-line", "pharmacotherapy", "for", "major", "depressive", "disorder", "."],
      ["O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "I-Disease", "O"])

    # Anxiety disorders
    s(["Generalized", "anxiety", "disorder", "involves", "persistent", "and", "excessive", "worry", "."],
      ["B-Disease", "I-Disease", "I-Disease", "O", "O", "O", "O", "O", "O"])

    # Bipolar disorder
    s(["Lithium", "is", "a", "mood", "stabilizer", "used", "for", "bipolar", "disorder", "."],
      ["O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    # Kidney stones
    s(["Recurrent", "kidney", "stones", "can", "lead", "to", "chronic", "kidney", "disease", "."],
      ["O", "B-Disease", "I-Disease", "O", "O", "O", "B-Disease", "I-Disease", "I-Disease", "O"])

    # Pancreatitis
    s(["Acute", "pancreatitis", "is", "often", "caused", "by", "gallstones", "or", "alcohol", "use", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    # Cirrhosis
    s(["Cirrhosis", "results", "from", "long-term", "liver", "damage", "caused", "by", "hepatitis", "B", "or", "alcohol", "."],
      ["B-Disease", "O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O", "O", "O"])

    # Thyroid cancer
    s(["Papillary", "thyroid", "cancer", "is", "the", "most", "common", "thyroid", "malignancy", "."],
      ["B-Disease", "I-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O"])

    # Cervical cancer
    s(["HPV", "vaccination", "prevents", "the", "majority", "of", "cervical", "cancer", "cases", "."],
      ["O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O", "O"])

    # Bladder cancer
    s(["Smoking", "is", "the", "primary", "risk", "factor", "for", "bladder", "cancer", "."],
      ["O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    # Esophageal cancer
    s(["Barrett", "esophagus", "is", "a", "precursor", "to", "esophageal", "cancer", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    # Gastric cancer
    s(["Helicobacter", "pylori", "infection", "is", "associated", "with", "gastric", "cancer", "."],
      ["O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    # Pancreatic cancer
    s(["Pancreatic", "cancer", "has", "a", "5-year", "survival", "rate", "below", "12%", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O"])

    # Hepatocellular carcinoma
    s(["Sorafenib", "is", "first-line", "therapy", "for", "advanced", "hepatocellular", "carcinoma", "."],
      ["O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    # Kidney cancer
    s(["Clear-cell", "renal", "cell", "carcinoma", "is", "the", "most", "common", "kidney", "cancer", "."],
      ["B-Disease", "I-Disease", "I-Disease", "I-Disease", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    # Brain tumor / glioblastoma
    s(["Glioblastoma", "multiforme", "is", "the", "most", "aggressive", "primary", "brain", "tumor", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O"])

    s(["Temozolomide", "combined", "with", "radiotherapy", "is", "standard", "for", "glioblastoma", "multiforme", "."],
      ["O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    # Meningitis
    s(["Bacterial", "meningitis", "is", "a", "medical", "emergency", "requiring", "immediate", "antibiotics", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O"])

    # Pneumococcal meningitis
    s(["Streptococcus", "pneumoniae", "is", "the", "leading", "cause", "of", "bacterial", "meningitis", "in", "adults", "."],
      ["O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O", "O", "O"])

    # Spinal muscular atrophy
    s(["Spinal", "muscular", "atrophy", "is", "caused", "by", "SMN1", "gene", "deletions", "."],
      ["B-Disease", "I-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O"])

    s(["Nusinersen", "is", "an", "antisense", "oligonucleotide", "therapy", "for", "spinal", "muscular", "atrophy", "."],
      ["O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "I-Disease", "O"])

    # Down syndrome
    s(["Down", "syndrome", "is", "caused", "by", "trisomy", "of", "chromosome", "21", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O"])

    # Sickle cell disease
    s(["Sickle", "cell", "disease", "results", "from", "a", "point", "mutation", "in", "the", "HBB", "gene", "."],
      ["B-Disease", "I-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    s(["Hydroxyurea", "reduces", "vaso-occlusive", "crises", "in", "sickle", "cell", "disease", "."],
      ["O", "O", "O", "O", "O", "B-Disease", "I-Disease", "I-Disease", "O"])

    # Thalassemia
    s(["Beta-thalassemia", "major", "requires", "regular", "blood", "transfusions", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O"])

    # Hemophilia
    s(["Hemophilia", "A", "results", "from", "deficiency", "of", "clotting", "factor", "VIII", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O"])

    # Marfan syndrome
    s(["Marfan", "syndrome", "is", "caused", "by", "mutations", "in", "the", "FBN1", "gene", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    # Fragile X syndrome
    s(["Fragile", "X", "syndrome", "is", "the", "most", "common", "inherited", "cause", "of", "intellectual", "disability", "."],
      ["B-Disease", "I-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    # Angelman syndrome
    s(["Angelman", "syndrome", "is", "characterized", "by", "intellectual", "disability", "and", "seizures", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O"])

    # Prader-Willi syndrome
    s(["Prader-Willi", "syndrome", "results", "from", "loss", "of", "paternal", "15q11-13", "gene", "expression", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    # Tuberous sclerosis
    s(["Tuberous", "sclerosis", "complex", "is", "associated", "with", "mTOR", "pathway", "overactivation", "."],
      ["B-Disease", "I-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O"])

    # Neurofibromatosis
    s(["Neurofibromatosis", "type", "1", "results", "from", "NF1", "gene", "mutations", "."],
      ["B-Disease", "I-Disease", "I-Disease", "O", "O", "O", "O", "O", "O"])

    # Wilson disease
    s(["Wilson", "disease", "causes", "copper", "accumulation", "in", "the", "liver", "and", "brain", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    # Gaucher disease
    s(["Gaucher", "disease", "is", "the", "most", "common", "lysosomal", "storage", "disorder", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O"])

    # Fabry disease
    s(["Fabry", "disease", "results", "from", "alpha-galactosidase", "A", "deficiency", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O"])

    # Pompe disease
    s(["Pompe", "disease", "involves", "glycogen", "accumulation", "in", "muscle", "cells", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O"])

    # Phenylketonuria
    s(["Phenylketonuria", "results", "from", "phenylalanine", "hydroxylase", "deficiency", "."],
      ["B-Disease", "O", "O", "O", "O", "O", "O"])

    # Galactosemia
    s(["Galactosemia", "is", "managed", "by", "strict", "galactose-free", "diet", "."],
      ["B-Disease", "O", "O", "O", "O", "O", "O", "O"])

    # Mixed-context sentences
    s(["The", "risk", "of", "breast", "cancer", "and", "ovarian", "cancer", "is", "elevated", "in", "BRCA1", "carriers", "."],
      ["O", "O", "O", "B-Disease", "I-Disease", "O", "B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O"])

    s(["Patients", "with", "rheumatoid", "arthritis", "are", "at", "increased", "risk", "for", "cardiovascular", "disease", "."],
      ["O", "O", "B-Disease", "I-Disease", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    s(["Comorbid", "depression", "worsens", "outcomes", "in", "chronic", "kidney", "disease", "."],
      ["O", "B-Disease", "O", "O", "O", "B-Disease", "I-Disease", "I-Disease", "O"])

    s(["Obesity", "is", "a", "risk", "factor", "for", "type", "2", "diabetes", ",", "hypertension", ",", "and", "atherosclerosis", "."],
      ["O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "I-Disease", "O", "B-Disease", "O", "O", "B-Disease", "O"])

    s(["Patients", "diagnosed", "with", "colorectal", "cancer", "should", "be", "screened", "for", "Lynch", "syndrome", "."],
      ["O", "O", "O", "B-Disease", "I-Disease", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    s(["Lynch", "syndrome", "predisposes", "to", "colorectal", "cancer", "and", "endometrial", "cancer", "."],
      ["B-Disease", "I-Disease", "O", "O", "B-Disease", "I-Disease", "O", "B-Disease", "I-Disease", "O"])

    s(["The", "co-occurrence", "of", "asthma", "and", "COPD", "is", "termed", "asthma-COPD", "overlap", "."],
      ["O", "O", "O", "B-Disease", "O", "B-Disease", "O", "O", "O", "O", "O"])

    s(["Both", "Crohn", "disease", "and", "rheumatoid", "arthritis", "may", "respond", "to", "anti-TNF", "agents", "."],
      ["O", "B-Disease", "I-Disease", "O", "B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O"])

    s(["The", "gene", "LRRK2", "is", "mutated", "in", "familial", "Parkinson", "disease", "."],
      ["O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    s(["Tau", "pathology", "is", "shared", "between", "Alzheimer", "disease", "and", "frontotemporal", "dementia", "."],
      ["O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O", "B-Disease", "I-Disease", "O"])

    s(["The", "FMR1", "gene", "repeat", "expansion", "underlies", "fragile", "X", "syndrome", "."],
      ["O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "I-Disease", "O"])

    s(["Checkpoint", "immunotherapy", "is", "used", "in", "melanoma", ",", "lung", "cancer", ",", "and", "bladder", "cancer", "."],
      ["O", "O", "O", "O", "O", "B-Disease", "O", "B-Disease", "I-Disease", "O", "O", "B-Disease", "I-Disease", "O"])

    s(["Lupus", "nephritis", "and", "rheumatoid", "arthritis", "are", "both", "autoimmune", "diseases", "."],
      ["B-Disease", "I-Disease", "O", "B-Disease", "I-Disease", "O", "O", "O", "O", "O"])

    s(["The", "prognosis", "of", "amyotrophic", "lateral", "sclerosis", "is", "worse", "than", "multiple", "sclerosis", "."],
      ["O", "O", "O", "B-Disease", "I-Disease", "I-Disease", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    s(["Both", "cystic", "fibrosis", "and", "sickle", "cell", "disease", "are", "autosomal", "recessive", "disorders", "."],
      ["O", "B-Disease", "I-Disease", "O", "B-Disease", "I-Disease", "I-Disease", "O", "O", "O", "O", "O"])

    s(["Epidemiological", "studies", "link", "hypertension", "to", "stroke", "and", "myocardial", "infarction", "."],
      ["O", "O", "O", "B-Disease", "O", "B-Disease", "O", "B-Disease", "I-Disease", "O"])

    s(["Urinary", "tract", "infection", "is", "common", "in", "elderly", "patients", "with", "type", "2", "diabetes", "."],
      ["B-Disease", "I-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "I-Disease", "O"])

    s(["Clostridium", "difficile", "infection", "is", "a", "nosocomial", "disease", "linked", "to", "antibiotic", "use", "."],
      ["B-Disease", "I-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    s(["Irritable", "bowel", "syndrome", "is", "distinct", "from", "inflammatory", "bowel", "disease", "."],
      ["B-Disease", "I-Disease", "I-Disease", "O", "O", "O", "B-Disease", "I-Disease", "I-Disease", "O"])

    s(["Psoriasis", "and", "psoriatic", "arthritis", "share", "overlapping", "inflammatory", "pathways", "."],
      ["B-Disease", "O", "B-Disease", "I-Disease", "O", "O", "O", "O", "O"])

    s(["Ankylosing", "spondylitis", "is", "strongly", "associated", "with", "the", "HLA-B27", "allele", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O"])

    s(["Gout", "results", "from", "hyperuricemia", "and", "monosodium", "urate", "crystal", "deposition", "."],
      ["B-Disease", "O", "O", "B-Disease", "O", "O", "O", "O", "O", "O"])

    s(["Paget", "disease", "of", "bone", "is", "associated", "with", "elevated", "alkaline", "phosphatase", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    s(["Acromegaly", "results", "from", "excess", "growth", "hormone", "secretion", "usually", "from", "a", "pituitary", "adenoma", "."],
      ["B-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O", "B-Disease", "I-Disease", "O"])

    s(["Cushing", "syndrome", "is", "caused", "by", "prolonged", "exposure", "to", "elevated", "cortisol", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    s(["Addison", "disease", "results", "from", "primary", "adrenal", "insufficiency", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O"])

    s(["Pheochromocytoma", "is", "a", "catecholamine-secreting", "tumor", "of", "the", "adrenal", "medulla", "."],
      ["B-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    s(["Myelodysplastic", "syndrome", "can", "progress", "to", "acute", "myeloid", "leukemia", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "B-Disease", "I-Disease", "I-Disease", "O"])

    s(["Multiple", "myeloma", "is", "a", "plasma", "cell", "malignancy", "causing", "bone", "destruction", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    s(["Waldenström", "macroglobulinemia", "is", "characterized", "by", "IgM", "paraprotein", "overproduction", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O"])

    s(["Chronic", "lymphocytic", "leukemia", "is", "the", "most", "common", "adult", "leukemia", "."],
      ["B-Disease", "I-Disease", "I-Disease", "O", "O", "O", "O", "O", "B-Disease", "O"])

    s(["Myelofibrosis", "is", "a", "clonal", "stem-cell", "disorder", "causing", "bone", "marrow", "fibrosis", "."],
      ["B-Disease", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"])

    s(["Polycythemia", "vera", "is", "associated", "with", "JAK2", "V617F", "mutations", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "O"])

    s(["Essential", "thrombocythemia", "increases", "the", "risk", "of", "thrombosis", "and", "stroke", "."],
      ["B-Disease", "I-Disease", "O", "O", "O", "O", "O", "O", "B-Disease", "O"])

    return data
