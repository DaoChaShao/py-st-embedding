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

1. Clone the repository.
2. Run the command `pip install -r requirements.txt`.
3. Run the application via the command `streamlit run main.py`.
4. Or, you can use it online >>> 