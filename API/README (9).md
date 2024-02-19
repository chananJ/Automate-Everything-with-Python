
# credit score

our project aims to classify borrowers and predict whether they will be considered good or bad loans based on their features.


## Authors

- [@Chanan Jacobs](https://github.com/chananJ)
- [@Aviv Yefet](https://github.com/avivyefet)



## the problem
Given a person's credit-card information, we will build a machine learning model that can classify the credit score. Our goal is to create a smart system with ML that can categorize individuals into class good or bad based on thier features.
In the project we will use the data of a global company that collected basic bank details and gathered a lot of credit-related information.


## the data
Our data is taken out of Kaggle. In the data there are various types of features . These features include both numerical and categorical variables. The dataset includes features such as customer demographics (age, gender, marital status), financial indicators (income, expenses, debt), credit history (number of previous loans, repayment behavior), employment details (occupation, employment length), and other relevant information.
- in the data we have: 1000 rows, 21 columns

#### the features
our dependent variable:
- class (good/bad) Represents the credit risk associated with the customer.

bullian features:
- own_telephone {none, yes}
- foreign_worker {yes, no}

Numeric Features:
- residence_since
- age
- duration
- credit_amount 

 Categorical Features:
- checking_status { no checking,<0, 0<=X<200,>=200}
- credit_history {no credits/all paid, existing paid, delayed previously, critical/other existing credit, all paid}
- Purpose {new car, education, furniture/equipment, radio/tv, used car, business, domestic appliance, repairs, other, retraining}
- savings_status {>=1000, <100, 500<=X<1000, no known savings, 100<=X<500}
- employment {unemployed, 1<=X<4, 4<=X<7, >=7, <1}
- personal_status {male single, female div/dep/mar, male div/sep, male mar/wid}
- other_parties {guarantor, none, co applicant}
- property_magnitude {unskilled resident, high qualif/self emp/mgmt, unemp/unskilled non res}
- installment_commitment {none, bank, stores}

- other_payment_plan  {none, bank, stores}
- housing {for free, own, rent}
- existing_credits {1, 2, 3, 4}
- job {skilled, unskilled resident, high qualif/self emp/mgmt, unemp/unskilled non res}
- num_depen {2, 1}



## Our project structure
- EDA report
- Data preparation 
- Application of Classification models
- evaluation of the models
- conclusions


## Appendix




 https://github.com/chananJ/Data-Science-/blob/main/creditRrisk_project.ipynb

 https://www.kaggle.com/datasets/ppb00x/credit-risk-customers
