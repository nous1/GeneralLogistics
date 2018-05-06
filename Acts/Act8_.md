
Meeting Content

* Tentative Supervised ML Development Layout for Classification
  1. Initial analisis
    * Main statistics (means, std, missings, counts)
    * Attribute distribution (pareto, normal, uniform, ...)
    * Per attribute Plots (satter for numerical, barplots for categorical)
      * Optional: Histograms following rules in 
        https://github.com/nous1/GeneralLogistics/blob/master/ManPages/TutorialLinks.md
  
  1. Data cleaning
    * Replace NaN values 
      * Mean/max/min in numeric values and Mode/weighted-probability in categorical.

  1. Initial attribute selection

  1. Initial algorithm testing (all models)

  1. Algorithm selection and training

  1. Algorithm finetuning
  .Botplox: Identificación de variación de datos numéricos en cuanto a datos categóricos;

  1. Presentación de hallazgos.
  
  1. Per class plots (boxplot for numerical, barplots for actegorical)
    1. Select important (critical for class separtation) attribute
    1. Plot attribute values for each class

* Considerations about what could need reinforcement
  * Data cleaning
  * Importance of attribute distribution
  * Learning algorithm finetuning
