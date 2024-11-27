from mmengine.config import read_base

with read_base():
    # from opencompass.configs.datasets.demo.demo_gsm8k_chat_gen import gsm8k_datasets
    # from opencompass.configs.datasets.demo.demo_math_chat_gen import math_datasets
    from opencompass.configs.datasets.cmb.cmb_gen import cmb_datasets
    from opencompass.configs.datasets.ceval.ceval_gen import ceval_datasets
    # from opencompass.configs.models.qwen.hf_qwen2_1_5b_instruct import models as hf_qwen2_1_5b_instruct_models
    # from opencompass.configs.models.hf_internlm.hf_internlm2_chat_1_8b import models as hf_internlm2_chat_1_8b_models
    from opencompass.configs.models.qwen2_5.hf_qwen2_5_7b_instruct import models as hf_qwen2_5_7b_instruct_models
    from opencompass.configs.models.qwen2_5.vllm_qwen2_5_7b_instruct import models as vllm_qwen2_5_7b_instruct

# datasets = cmb_datasets
datasets = ceval_datasets
models = vllm_qwen2_5_7b_instruct
