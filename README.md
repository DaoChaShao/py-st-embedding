**Introduction**  
This application is used to practice how to use the plotly chart demonstrating features of vocabularies.

**How to reduce the dimension of the data**

1. **PCA**
    - Set the data, which is more than at least 3 dimensions.
    - Use the PCA method to reduce the dimension of the data.
    - The PCA method is more suitable for the data that has a linear relationship.
2. **t-SNE**
    - Set the data, which is more than at least 3 dimensions.
    - Use the t-SNE method to reduce the dimension of the data.
    - The t-SNE method is more suitable for the data that has a non-linear relationship.
    - However, the t-SNE method is more time-consuming than the PCA method.
3. **UMAP**
    - Set the data, which is more than at least 3 dimensions.
    - Use the UMAP method to reduce the dimension of the data.
    - The UMAP method is more suitable for the data that has a non-linear relationship.
    - The UMAP method is faster than the t-SNE method.

**How to use the application**

1. The reference page
   is [ModelScope](https://www.modelscope.cn/models/iic/nlp_gte_sentence-embedding_chinese-large/summary). However, it
   is not so helpful. You need to add many dependencies to run the application except the dependency of modelscope.
2. Clone the repository.
3. Run the command `pip install modelscope`.
4. Run the command `pip install addict`.
5. Run the command `pip install setuptools` to add the new dependency.
6. Run the command `pip install datasets` to add the new dependency, which is normally provided
   by [Hugging Face](https://huggingface.co/).
7. Run the command `pip install torch` to add the new dependency.
8. Run the command `pip install simplejson` to add the new dependency.
9. Run the command `pip install sortedcontainers` to add the new dependency.
10. Run the command `pip install transformers` to add the new dependency.
9. Run the application via the command `streamlit run main.py`.
10. Or, you can run the command `pip install -r requirements.txt` to install all dependencies.
11. Or, you can use it online >>> 