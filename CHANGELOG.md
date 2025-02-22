<!-- insertion marker -->
<a name="0.1.0"></a>

## [0.1.0](https://github.com/DaoChaShao/py-st-embedding/compare/36081daabae33f6560bc7c61214158f7d738e897...0.1.0) (2025-02-22)

### Features

- enhance embedding visualization with query comparison and sidebar interaction ([685ff30](https://github.com/DaoChaShao/py-st-embedding/commit/685ff30f02935d30150b6d13fb91972626b910c3))
- implement sentence embedding model selection with modelscope ([65f1e87](https://github.com/DaoChaShao/py-st-embedding/commit/65f1e8735dec41e7026ac2934423b4c7298b09fc))
- add sidebar for embedding model configuration with hyperparameters ([c68f7ff](https://github.com/DaoChaShao/py-st-embedding/commit/c68f7ffcca478bfed895da8feaf4689f41f3fef9))
- update requirements.txt with additional dependencies for improved functionality ([8d09a89](https://github.com/DaoChaShao/py-st-embedding/commit/8d09a89c6098fde6021b257d0bb7ac9614189793))
- add modelscope and pip requirements for enhanced functionality ([3820d22](https://github.com/DaoChaShao/py-st-embedding/commit/3820d2257d226a95dc259b25ef3b67601ef1b30b))
- enhance UMAP parameters with feature dimensions, point size, and font size captions ([f6ba497](https://github.com/DaoChaShao/py-st-embedding/commit/f6ba497d7b53b7556db13c35f2fe325eb98bbe59))
- update 3D UMAP to accept feature dimensions, point size, and font size parameters ([274b6dc](https://github.com/DaoChaShao/py-st-embedding/commit/274b6dc4bc4b52ae50820351f5252df094eb356a))
- add customizable point and font sizes to 3D scatter plot function ([470c398](https://github.com/DaoChaShao/py-st-embedding/commit/470c3985263753b9931416599a949574086dce59))
- add PCA parameter sliders for feature dimensions, point size, and font size ([ee52309](https://github.com/DaoChaShao/py-st-embedding/commit/ee5230946ea5fc06e279a35a414794c296b68a54))
- integrate customizable parameters for PCA scatter plot ([7e66b6b](https://github.com/DaoChaShao/py-st-embedding/commit/7e66b6b17d29a0952356fe42e01766e917ea2d23))
- add sidebar parameters for 3D scatter visualization ([c9c5a3a](https://github.com/DaoChaShao/py-st-embedding/commit/c9c5a3a1c96f70648946e5e6f610dc25c3377680))
- add parameter setup functions for 2D scatter and update imports ([9472406](https://github.com/DaoChaShao/py-st-embedding/commit/94724062469919ccf7d55be614a1840888443895))
- add the model tools. ([5570962](https://github.com/DaoChaShao/py-st-embedding/commit/55709626a1ab10d577ac5beaec31a282a1fd339f))
- add the embedding model test page. ([08e5134](https://github.com/DaoChaShao/py-st-embedding/commit/08e51341e49eaa9a889f63d0e683fa43128eaf6e))
- add the new page for demonstrating vectors visualization via UMAP. ([5e52302](https://github.com/DaoChaShao/py-st-embedding/commit/5e52302dd5601bfcd024122fb57b5c1fd50c681f))
- add the subpage and navigation bar. ([b6d855d](https://github.com/DaoChaShao/py-st-embedding/commit/b6d855d23ba16d8aa29f39a5fe325798ae0031c1))
- restruct the page architecture. ([b78d8e7](https://github.com/DaoChaShao/py-st-embedding/commit/b78d8e73d3cd90417b38999d9cbc1dad94cbc681))
- update the new functions. ([efc6de3](https://github.com/DaoChaShao/py-st-embedding/commit/efc6de3f7a75e72704548fdd3f6626984a06ca13))
- rebuild the previous datasets, and add the new ones. ([5b78884](https://github.com/DaoChaShao/py-st-embedding/commit/5b78884c85fbbeb5dc6c3d20c92291b327281393))
- initialize database. ([8503729](https://github.com/DaoChaShao/py-st-embedding/commit/850372949e007b57f0a79f6877aa500d05f6bf41))
- rebuild all the functions via plotly. ([b9b2ffc](https://github.com/DaoChaShao/py-st-embedding/commit/b9b2ffc799aee805e300453a374c11a77799ee0c))
- create a toolkit. ([b8747f4](https://github.com/DaoChaShao/py-st-embedding/commit/b8747f4e7de499979b081a973aa418fc18349aee))
- create the main file. ([8469b0e](https://github.com/DaoChaShao/py-st-embedding/commit/8469b0e8e58b842c18e102cbca0d49cb32c97104))
- add the configration file for changing log. ([3e20c9a](https://github.com/DaoChaShao/py-st-embedding/commit/3e20c9a314e72e5a4966136e9909f36bb3876cfb))
- add the ignore file. ([b645991](https://github.com/DaoChaShao/py-st-embedding/commit/b645991c5c521505a4f028b11e8012045e1df37f))

### Bug Fixes

- rename "Embedding Model" to "Models" for clarity in layout ([404bd22](https://github.com/DaoChaShao/py-st-embedding/commit/404bd2276961c14cd9e748c66b20a90b32d6fa59))
- rename "Reality" to "Simulation" for improved accuracy in layout ([e7b44b0](https://github.com/DaoChaShao/py-st-embedding/commit/e7b44b0c4de39cce6dd8e234668fcbcd9254a632))
- rename parameter for feature data generation to improve clarity ([1beea83](https://github.com/DaoChaShao/py-st-embedding/commit/1beea83893a77840147741b2d131d3d42b9fe442))
- enhance 3D scatter plot with customizable point and font sizes ([5f63194](https://github.com/DaoChaShao/py-st-embedding/commit/5f63194a66a30eec3d79fbc97477b30d52e21e7c))
- update imports ([df8f807](https://github.com/DaoChaShao/py-st-embedding/commit/df8f8070721289c165dd937fc908aa233327704e))
- correct import path for subpages_setter in main.py ([0d08f72](https://github.com/DaoChaShao/py-st-embedding/commit/0d08f7257df953db67aecacd125c591c98d4e4d5))
- downgrade numpy version to 2.1.3 in requirements.txt ([078c6d3](https://github.com/DaoChaShao/py-st-embedding/commit/078c6d31fd6174110c8cf300abe47f0c88cd3990))
- update imports and enhance scatter plot parameters ([fb4b9b8](https://github.com/DaoChaShao/py-st-embedding/commit/fb4b9b8d07672961feb200c0bc231be3e06d7a96))

### Chore

- update CHANGELOG.md for version 0.1.0 with new features, bug fixes, and improvements ([a23c39f](https://github.com/DaoChaShao/py-st-embedding/commit/a23c39fcc0d18e5eea4d8d7d6920e78751ba0eb8))
- register the embedding page on the application. ([5dabe90](https://github.com/DaoChaShao/py-st-embedding/commit/5dabe905d9429c9e68a1f30690472ac2cb945059))
- use the new functions. ([229e324](https://github.com/DaoChaShao/py-st-embedding/commit/229e32486ad2946fe067f85cba2c596e571e8499))
- use the new tools. ([147cec7](https://github.com/DaoChaShao/py-st-embedding/commit/147cec7f7b1f85ec540fdb9cb6da241e6123b6cd))
- add the 2d chart, but 3d is filed. ([1912762](https://github.com/DaoChaShao/py-st-embedding/commit/1912762a8e0d674c6f83d2ece3caadb620dc3cad))

### Docs

- update README with detailed installation instructions and additional dependencies ([0ead368](https://github.com/DaoChaShao/py-st-embedding/commit/0ead368c8bf4b0c6c05ffbeb2ebe5cff704df4af))
- expand README with dimensionality reduction methods and usage instructions ([4f75664](https://github.com/DaoChaShao/py-st-embedding/commit/4f75664d41dfeaf195fd4ea7bc3910308eccd6aa))
- create LICENSE ([ce049b5](https://github.com/DaoChaShao/py-st-embedding/commit/ce049b5a44e26acad81cf6706bc9301187eba3fa))
- update CHANGELOG.md. ([d4b0e0d](https://github.com/DaoChaShao/py-st-embedding/commit/d4b0e0d9e8c00508e6bcf2bebce48f88873bb445))
- update CHANGELOG.md ([6c4e31b](https://github.com/DaoChaShao/py-st-embedding/commit/6c4e31b0f3e4e8bd8fc01aea79b929cd76e0d4d7))
- create the README.md. ([0bcfb27](https://github.com/DaoChaShao/py-st-embedding/commit/0bcfb27c9cd8b6beb5f8b6e651c6c5cd7dad7ebd))
- create the file of changing log. ([0cf83a7](https://github.com/DaoChaShao/py-st-embedding/commit/0cf83a75794b621717f00347442021e9c3498869))

### Performance Improvements

- enhance the function of generating random data. ([2b5770c](https://github.com/DaoChaShao/py-st-embedding/commit/2b5770c08e98810d686cdc90f04aeb4d3000e619))
- restruct the main function to optimize the performance. ([ae4fbea](https://github.com/DaoChaShao/py-st-embedding/commit/ae4fbea4be2baaf1a297434f6fda689913dcc671))
- add the normal function. ([6323dd9](https://github.com/DaoChaShao/py-st-embedding/commit/6323dd9fde109ed3766e72d2f44ea86be61dc78b))
- enhance the generating ability of the datasets. ([aaa091f](https://github.com/DaoChaShao/py-st-embedding/commit/aaa091f0a9ef0b8aa202037118394c1a378d1dc4))
- update the functions capability to handle more complex scenarios. ([4db6ffe](https://github.com/DaoChaShao/py-st-embedding/commit/4db6ffe894f932cb02820a3314fc34fd27c6b49f))
- restruct the coding architecture of the project. ([f132711](https://github.com/DaoChaShao/py-st-embedding/commit/f13271115f76e7fa259b1d9d7caecab6d3e58450))
- add the new functions and improve the previous functions. ([0cef91f](https://github.com/DaoChaShao/py-st-embedding/commit/0cef91fc9875d44b982edb7b637e82776de0d871))

### Dependencies

- add the new dependency, which is umap-learn package. ([6dad183](https://github.com/DaoChaShao/py-st-embedding/commit/6dad183c4d7c85161a6982e6bc6bcf9a5cc87bac))
- dislodge unnecessary dependencies. ([4a23a35](https://github.com/DaoChaShao/py-st-embedding/commit/4a23a355ee670454b6de3eb3b0f5e206b4b7c3f0))
- update dependencies. ([3c3e3f3](https://github.com/DaoChaShao/py-st-embedding/commit/3c3e3f3a9025727a4553c9be016ed12ba7f9689f))
- create the file of dependencies. ([018e9a6](https://github.com/DaoChaShao/py-st-embedding/commit/018e9a666e4adc95bc56f007f5f3edcef6e7127a))

