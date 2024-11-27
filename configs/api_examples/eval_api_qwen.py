from mmengine.config import read_base
from opencompass.models import Qwen
from opencompass.partitioners import NaivePartitioner
from opencompass.runners.local_api import LocalAPIRunner
from opencompass.tasks import OpenICLInferTask

with read_base():
    from opencompass.configs.summarizers.medium import summarizer
    from opencompass.configs.datasets.ceval.ceval_gen import ceval_datasets

datasets = [
    *ceval_datasets,
]

models = [
    dict(
        abbr='Qwen2.5-7B-Instruct',
        type=Qwen,
        path="http://10.5.10.8:8999/v1",
        key='sk-05e2dd6275a9187c77faccfdc730d352',
        generation_kwargs={
            'enable_search': False,
        },
        query_per_second=1,
        max_out_len=2048,
        max_seq_len=2048,
        batch_size=4
    ),
]

infer = dict(
    partitioner=dict(type=NaivePartitioner),
    runner=dict(
        type=LocalAPIRunner,
        max_num_workers=1,
        concurrent_users=1,
        task=dict(type=OpenICLInferTask)),
)

work_dir = 'outputs/api_qwen/'
