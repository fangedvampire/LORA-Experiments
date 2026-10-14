"""LoRA (Low-Rank Adaptation) learning toolkit.

Modules are added phase by phase:

- ``lora_layer``         : from-scratch PyTorch LoRA layer          (Phase 3)
- ``parameter_analysis`` : parameter / storage-size calculators      (Phase 4)
- ``utils``              : seeding, config loading, dataset building (Phase 5)
- ``train``              : Hugging Face PEFT training                (Phase 5)
- ``evaluate``           : perplexity + qualitative generation       (Phase 5)
- ``inference``          : load base model + adapter and generate    (Phase 5)
"""

__version__ = "0.1.0"