# Curated Scholarly Papers on AI-Assisted vs. Manual Data Labelling

## 1. Surveys and Foundational Frameworks
- **A Survey on Active Learning and Human-in-the-Loop Deep Learning for Medical Image Analysis**  
  *Budd, S., Robinson, E. C., & Glocker, B. (2021)* — *Medical Image Analysis*  
  [DOI: 10.1016/j.media.2021.102063](https://doi.org/10.1016/j.media.2021.102063)  
  *Comprehensive foundational review of uncertainty sampling, active learning cycles, and annotation cost reduction in clinical imaging.*
- **A Comprehensive Survey on Deep Active Learning in Medical Image Analysis**  
  *Wang, H., Jin, Q., Li, S., Liu, S., Wang, M., & Song, Z. (2024)* — *Medical Image Analysis*  
  [DOI: 10.1016/j.media.2024.103201](https://doi.org/10.1016/j.media.2024.103201)  
  *Taxonomy of representativeness- and uncertainty-based querying algorithms and foundation model integrations to overcome medical manual data labeling bottlenecks.*
- **Transforming Data Annotation with AI Agents: A Review of Methods, Tools, and Challenges**  
  *Liu, Y., et al. (2025)* — *Computers*  
  [DOI: 10.3390/computers14020042](https://doi.org/10.3390/computers14020042)  
  *Analyzes modern AI agent architectures, pre-annotation pipelines, and automated verification protocols across domain-specific annotation environments.*
- **Human-in-the-Loop Machine Learning**  
  *Monarch, R. M. (2021)* — *Manning Publications*  
  [Manning Book Reference](https://www.manning.com/books/human-in-the-loop-machine-learning)  
  *Foundational reference text defining inter-annotator agreement metrics, annotation quality control, and human-in-the-loop active learning strategies.*

## 2. AI vs. Human / Zero-Shot Empirical Accuracy Benchmarks
- **A Comparative Study of Zero-Shot Inference with Large Language Models and Supervised Modeling in Breast Cancer Pathology Classification**  
  *Sushil, M., Zack, T., Mandair, D., Zheng, Z., Wali, A., Yu, Y.-N., Quan, Y., & Butte, A. J. (2024)* — *arXiv* / *Journal of Clinical Oncology*  
  [DOI: 10.48550/arxiv.2401.13887](https://doi.org/10.48550/arxiv.2401.13887)  
  *Empirically benchmarks zero-shot LLM inference directly against human expert-annotated ground truth and supervised classifiers on unstructured pathology reports.*
- **Accurate Medical Named Entity Recognition Through Specialized NLP Models**  
  *Hu, J., Bao, R., Lin, Y., Zhang, H., & Xiang, Y. (2024)* — *arXiv*  
  [DOI: 10.48550/arxiv.2412.08255](https://doi.org/10.48550/arxiv.2412.08255)  
  *Compares specialized domain transformers (BioBERT, SciBERT) to evaluate span-level accuracy against human gold standards on biomedical corpora.*
- **Harnessing Large Language Models’ Zero-Shot and Few-Shot Learning Capabilities for Regulatory Research**  
  *Meshkin, H., Zirkle, J., Arabidarrehdor, G., et al. (2024)* — *Briefings in Bioinformatics*  
  [DOI: 10.1093/bib/bbae354](https://doi.org/10.1093/bib/bbae354)  
  *Quantifies zero- and few-shot LLM categorization accuracy on complex bio-regulatory texts compared to human specialist curation.*
- **Comparing Human and Machine Annotations for Complex Scientific Information Extraction**  
  *Wadden, D., Lin, S., Lo, K., et al. (2022)* — *Findings of the ACL: EACL 2022*  
  [DOI: 10.18653/v1/2022.findings-eacl.84](https://doi.org/10.18653/v1/2022.findings-eacl.84)  
  *Examines disagreement rates and structural accuracy divergences between domain-expert annotations and machine learning models on scientific claim extraction.*

## 3. Active Learning and Interactive Annotation Methods
- **A Study of Deep Active Learning Methods to Reduce Labelling Efforts in Biomedical Relation Extraction**  
  *Nachtegael, C., De Stefani, J., & Lenaerts, T. (2023)* — *PLOS ONE*  
  [DOI: 10.1371/journal.pone.0292356](https://doi.org/10.1371/journal.pone.0292356)  
  *Demonstrates that uncertainty sampling reduces manual curation workload by 6% to 38% on biomedical relation extraction datasets.*
- **Interactive Machine Learning for Health Informatics: When Do We Need the Human-in-the-Loop?**  
  *Holzinger, A. (2016)* — *Brain Informatics*  
  [DOI: 10.1007/s40708-016-0042-6](https://doi.org/10.1007/s40708-016-0042-6)  
  *Outlines theoretical criteria where high-complexity biomedical data strictly demands human-in-the-loop expert adjudication over full automation.*
- **Transformer-Based Active Learning for Multi-Class Text Annotation in Clinical Notes**  
  *Al-Garadi, M. A., Yang, Y. C., & Sarker, A. (2024)* — *Scientific Reports (Nature)*  
  [DOI: 10.1038/s41598-024-74895-x](https://doi.org/10.1038/s41598-024-74895-x)  
  *Evaluates transformer-driven active learning pipelines on clinical datasets, assessing reductions in physician manual annotation burden.*
- **Active Learning for Biomedical Article Classification with Bag-of-Entities**  
  *Przybyła, P. (2024)* — *Applied Sciences*  
  [DOI: 10.3390/app14177945](https://doi.org/10.3390/app14177945)  
  *Evaluates query strategies (uncertainty vs. diversity) to accelerate systematic biomedical document curation while preserving classification recall.*

## 4. Annotation Quality, Inter-Rater Agreement and Human Biases
- **Automation Bias in Intelligent Clinical Decision Support Systems: A Systematic Review**  
  *Goddard, K., Roudsari, A., & Wyatt, J. C. (2012)* — *International Journal of Medical Informatics*  
  [DOI: 10.1016/j.ijmedinf.2011.10.008](https://doi.org/10.1016/j.ijmedinf.2011.10.008)  
  *Evaluates cognitive errors where human annotators unthinkingly accept incorrect automated suggestions in AI-assisted workflows.*
- **Creating a Benchmark for Field-Specific Biomedical Named Entity Recognition: Inter-Annotator Agreement Assessment**  
  *Brandsen, A., Verberne, S., Lambers, K., & Wansleeben, M. (2020)* — *Proc. BioNLP Workshop (ACL)*  
  [DOI: 10.18653/v1/2020.bionlp-1.18](https://doi.org/10.18653/v1/2020.bionlp-1.18)  
  *Details boundary discrepancies and Cohen's kappa statistics between domain experts annotating technical scientific terminology.*
- **Learning from Disagreement: A Survey on Human Label Variation**  
  *Uma, A. N., Fornaciari, T., Dumitrache, A., et al. (2021)* — *Journal of Artificial Intelligence Research (JAIR)*  
  [DOI: 10.1613/jair.1.12752](https://doi.org/10.1613/jair.1.12752)  
  *Analyzes inherent variability in expert human annotations and models disagreement beyond simple majority voting.*
- **Crowdsourcing and Federated Labeling in Digital Pathology**  
  *Amgad, M., Elfandy, H., Hussein, H., et al. (2019)* — *Modern Pathology*  
  [DOI: 10.1038/s41379-019-0252-y](https://doi.org/10.1038/s41379-019-0252-y)  
  *Compares data quality and accuracy across novice crowd-workers, pathology residents, and deep-learning segmentation models.*

## 5. Domain Applications and Multimodal Frontiers
- **Benchmarking Large Language Models for Entity Resolution and Information Extraction in Materials Science**  
  *Shetty, P., et al. (2023)* — *Digital Discovery (RSC)*  
  [DOI: 10.1039/D3DD00055J](https://doi.org/10.1039/D3DD00055J)  
  *Compares zero-shot LLMs against domain-fine-tuned models for extracting complex synthesis parameters from unstructured chemistry and materials papers.*
- **Weakly Supervised Natural Language Processing for Scientific Document Information Extraction**  
  *Saier, T., & Färber, M. (2020)* — *Scientometrics*  
  [DOI: 10.1007/s11192-020-03612-4](https://doi.org/10.1007/s11192-020-03612-4)  
  *Assesses programmatic weak supervision against manual curation for generating structured citation and metadata datasets from scientific literature.*
- **Segment Anything Model for Medical Image Analysis: An Experimental Study**  
  *Mazurowski, M. A., Dong, H., Gu, H., et al. (2023)* — *Medical Image Analysis*  
  [DOI: 10.1016/j.media.2023.102918](https://doi.org/10.1016/j.media.2023.102918)  
  *Rigorous evaluation of prompt-based foundation segmentation models against expert radiologist ground truth across 19 medical imaging datasets.*
- **Segment Anything in Medical Images (MedSAM)**  
  *Ma, J., He, Y., Li, F., Han, L., You, C., & Wang, B. (2024)* — *Nature Communications*  
  [DOI: 10.1038/s41467-024-44824-z](https://doi.org/10.1038/s41467-024-44824-z)  
  *Demonstrates how specialized foundation models accelerate human clinician segmentation workflows across 1.5M+ medical image-mask pairs.*