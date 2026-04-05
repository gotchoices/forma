# Models

<!--EC
- The goal of this folder is to hold descriptions for different models of the MaSt Material sheets.
- Each model will have its own markdown file in this folder.
- Up until now, we have just built study after study and then updated documentation files across the repo ad hoc with our best knowledge up to that time.
  - For example, the root folder contains files that report the achievements of "the model"
  - We might also be making similar reports in various primers, papers, etc.
- By defining separate models, we can preserve the state of older models and still move on to new, improved models.
- Migration steps (suggested):
  - Model: torus_wvm (before mast terminology)
    Roughly correlated to studies S1 - S3, maybe a few after.
    This focused on the WvM model and tried to make all particles work on a single sheet.
    File can be fairly brief.  Explain what was tried and accomplished.
  - Model: torus_3
    Roughly correlated to the use of studies/lib/ma.py
    Review generally the process of trying to pin various values based on particle search.
    What was accomplished.
  - Model: mast_a
    Roughly correlated to the use of studies/lib/ma_model.py.
    Up through about study R44.
    Tested many more phenomena.  Explain generally and then iterate accomplishments, predictions, etc.
    Files currently in repo root that report model performance should have applicable details merged into this file.
  - Model: mast_b
    In process (see R46 and on).
    Going back to basics.  Re-model electron, proton, neutrino from scratch, no assumptions.
    Hope to do a new particle survey soon.
- Once global model performance data has been moved into mast_b, we then strip detailed data from root (particle lists, tables of predictions, long performance narratives) and replace with links into `models/`. Root still states which model is current (e.g. mast_c), a short one-line characterization, and pointers to the model file—not a blank or model-agnostic root.
- For example, someone reading the root/README would see that the current model is mast_c and what it is trying to do at a high level, but would open the mast_c model file for particle lists, specific prediction data, and full narrative.
- Once migration is done, ideally, we would not need to revise long root/README sections every time the current model progresses; we would mostly update the corresponding model markdown and only bump root when the “current model” identity or top-level pointer needs to change.

-->
