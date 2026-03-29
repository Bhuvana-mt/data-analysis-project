# data-analysis-project
A Python data analysis learning project with entertainment data

# Entertainment Data Analysis Project

## 📊 Project Overview
This project analyzes entertainment data from TMDB (The Movie Database) containing 5000+ movies. It performs data exploration, cleaning, statistical analysis, and creates visualizations to understand movie ratings, runtime, budgets, and revenues.

## 🎯 Objectives
- Load and explore movie dataset
- Clean data by removing missing values
- Perform statistical analysis on movie metrics
- Create visualizations to identify trends and patterns
- Generate analysis dashboard

## 📁 Project Structure
```
data-analysis-project/
├── data/
│   └── tmdb_5000_movies.csv          # TMDB dataset (5000 movies)
├── analysis.py                        # Main analysis script
├── analysis_dashboard.png             # Generated visualization
├── README.md                          # Project documentation
└── venv/                              # Virtual environment
```

## 🛠️ Technologies Used
- **Python 3.13** - Programming language
- **pandas** - Data manipulation and analysis
- **numpy** - Numerical computations
- **matplotlib** - Data visualization
- **seaborn** - Advanced plotting
- **scikit-learn** - Machine learning library
- **jupyter** - Interactive notebooks

## 📦 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/bhuvana-mt/data-analysis-project.git
cd data-analysis-project
```

### 2. Create Virtual Environment
```bash
python -m venv venv
```

### 3. Activate Virtual Environment
```bash
# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 4. Install Required Packages
```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

## 🚀 Running the Analysis

```bash
python analysis.py
```

**Output:**
- Prints dataset information and statistics to console
- Generates `analysis_dashboard.png` with 4 visualizations
- Displays interactive graph window

## 📊 Analysis Details

### Data Exploration
- Dataset shape: 5000 rows × multiple columns
- Key columns: vote_average, runtime, budget, revenue
- Missing values: Identified and handled

### Data Cleaning
- Removed rows with missing ratings or runtime values
- Handled data type conversions

### Statistical Analysis
- Average movie rating
- Average movie runtime
- Total number of movies
- Distribution analysis

### Visualizations Generated
1. **Rating Distribution** - Histogram showing frequency of movie ratings
2. **Runtime Distribution** - Histogram showing frequency of movie duration
3. **Rating vs Runtime** - Scatter plot showing relationship between duration and rating
4. **Budget vs Revenue** - Scatter plot showing financial performance

## 📈 Key Findings
- Most movies have ratings between 5-8
- Average runtime is approximately 100-110 minutes
- Runtime and rating show weak to moderate correlation
- Budget and revenue are positively correlated

## 👤 Author
**Bhuvana**

## 📝 License
This project is open source and available under the MIT License.

## 🔗 Links
- GitHub Repository: https://github.com/bhuvana-mt/data-analysis-project
- TMDB Dataset: https://www.kaggle.com/tmdb/tmdb-movie-metadata

## 💡 Future Enhancements
- Add genre-based analysis
- Perform sentiment analysis on reviews
- Build machine learning models for rating prediction
- Create interactive dashboard with Streamlit
- Add time-series analysis for release trends
