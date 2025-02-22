from modelscope.models import Model
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks


def model_cn_embedding_sentences(model_id: str, sequence_length: int):
    """
    Select the embedding model for Chinese sentences
        https://www.modelscope.cn/models/iic/nlp_gte_sentence-embedding_chinese-large/summary
    :param model_id: The model ID for the embedding
    :param sequence_length: The sequence length for the model
    :return: The pipeline for embedding sentences
    """
    pipeline_sentences = pipeline(
        Tasks.sentence_embedding,
        model=model_id,
        sequence_length=sequence_length,
    )
    return pipeline_sentences
