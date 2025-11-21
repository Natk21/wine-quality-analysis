This project analyzes the Red Wine Quality dataset, examining the distribution of wine quality scores, exploring feature relationships, and identifying chemical patterns linked to high- and low-quality wines. 
After loading and validating the dataset, I segmented wines into quality tiers and calculated their proportions, then visualized overall quality distribution using count plots. 

I graphed numerous features of the data set, outlined below:
<img width="640" height="480" alt="Figure 1" src="https://github.com/user-attachments/assets/7c86e167-f8e6-49d3-96f6-5f1c607fc495" />

This is a heatmap exploring the correlation between various variables in the wine dataset. A high correlation is signified by a deeper red.
<img width="1512" height="782" alt="Figure 2" src="https://github.com/user-attachments/assets/07c7a425-bc2e-45fa-9f00-6d3faa9ce22b" />

This explored the relationship between fixed acidity and ph for wine quality. A clear inverse relationship was observed
<img width="600" height="600" alt="Figure_3" src="https://github.com/user-attachments/assets/c9270986-9cf7-4d60-80b1-905d2e3c24c6" />

I then explored the relationship between fixed acidity and citric acid. This on the other hand produced a positive correlation. 
<img width="600" height="600" alt="Figure_4" src="https://github.com/user-attachments/assets/66a0e13f-8744-4f07-b6ac-6fe2c374b0af" />

<img width="1000" height="600" alt="Figure_5" src="https://github.com/user-attachments/assets/5fb80319-b0bf-4062-8411-fcfb9e4833b3" />

<img width="1000" height="600" alt="Figure_6" src="https://github.com/user-attachments/assets/49c4add6-f6b6-4696-aa61-56ade026cb91" />

Finally, I performed an outlier analysis for every feature using interquartile ranges to detect extreme chemical measurements that may influence model performance or skew statistical patterns.
