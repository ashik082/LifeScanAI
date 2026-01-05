## Model Training

This folder contains the code and dataset used to train the heart disease prediction model.

- Dataset: Large-scale heart disease dataset (~300k records)
- Algorithm: Logistic Regression
- Train-Test Split: 80% training, 20% testing
- Preprocessing: Label Encoding and Feature Scaling

The trained model (`heart_model.pkl`) and scaler (`scaler.pkl`) are exported and used in the backend Flask application for inference.

### Data Encoding Reference

#### Age Category
| Value | Age Range |
|-------|-----------|
| 0 | 18–24 |
| 1 | 25–29 |
| 2 | 30–34 |
| 3 | 35–39 |
| 4 | 40–44 |
| 5 | 45–49 |
| 6 | 50–54 |
| 7 | 55–59 |
| 8 | 60–64 |
| 9 | 65–69 |
| 10 | 70–74 |
| 11 | 75–79 |
| 12 | 80 or older |

#### Race
| Value | Race |
|-------|------|
| 0 | American Indian / Alaska Native |
| 1 | Asian |
| 2 | Black |
| 3 | Hispanic |
| 4 | Other |
| 5 | White |

#### General Health
| Value | Status |
|-------|--------|
| 0 | Poor |
| 1 | Fair |
| 2 | Good |
| 3 | Very Good |
| 4 | Excellent |

#### Physical Health (Days in past 30 days)
| Value | Description |
|-------|-------------|
| 0 | No physical health issues |
| 1–10 | Mild physical health problems |
| 11–20 | Moderate physical health problems |
| 21–30 | Severe physical health problems |

#### Mental Health (Days in past 30 days)
| Value | Description |
|-------|-------------|
| 0 | No mental stress |
| 1–10 | Mild mental stress |
| 11–20 | Moderate mental stress |
| 21–30 | Severe mental stress |


