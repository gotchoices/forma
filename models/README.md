# Models

<!--EC
- The goal of this folder is to hold descriptions for different models of the MaSt Material sheets.
- Each model will have its own markdown file in this folder.
- Up until now, we have just built study after study and then updated documentation files across the repo ad hoc with our best knowledge up to that time.
  - For example, the root folder contains files that report the achievements of "the model"
  - We might also be making similar reports in various primers, papers, etc.
- By defining separate models, we can preserve the state of older models and still move on to new, improved models.
- Migration steps (suggested):
  - Model: torus_wvm
    Roughly correlated to studies S1 - S3, maybe a few after.
    This focused on the WvM model and tried to make all particles work on a single sheet.
    File can be fairly brief.
  - Model: mast_a
    Roughly correlated to the use of studies/lib/ma.py
  - Model: mast_b
    Roughly correlated to the use of studies/lib/ma_model.py.
    Up through about study R44.
    Files currently in repo root that report model performance should be merged into this file.
  - Model: mast_c
    In process (see R46 and on).
    Going back to basics.  Re-model electron, proton, neutrino from scratch, no assumptions.
    Hope to do a new particle survey soon.
- Once global model performance data has been moved into mast_b, we then strip those specific data from direct presentation and instead provide hot links to the relevant files inside the models folder.
- For example, someone reading the root/README would read about general model performance such as "the current model (mast_c) predicts this many particles and this or that phenomenon) but they would not see things like particle lists or specific prediction data without clicking into the individual model file.
- Once migration is done, ideally, we would not need to update the root/README and similar files every time the current model progresses.
  We could instead just update the model file itself.

-->
