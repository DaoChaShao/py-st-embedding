from modelscope.models import Model
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks


def model_cn_embedding_sentences(model_id: str, sequence_length: int):
    """ Select the model for embedding """
    pipeline_sentences = pipeline(
        Tasks.sentence_embedding,
        model=model_id,
        sequence_length=sequence_length,
    )
    return pipeline_sentences
