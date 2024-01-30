#!/usr/bin/env python
# coding: utf-8

# In[1]:


from libraries import *


# In[2]:


def explore_data(data):
    shape = data.shape
    print("Number of rows:", shape[0])
    print("Number of columns:", shape[1])


# In[3]:


def display_dataframe_info(data):
    # Display information about the DataFrame
    data.info()


# In[4]:


def display_missing_values(data):
    # Display the count of missing values in each column
    missing_values = data.isnull().sum()
    print("Missing values in each column:")
    print(missing_values)


# In[5]:


def display_descriptive_statistics(data):
    # Display descriptive statistics of the DataFrame
    descriptive_stats = data.describe()
    print("Descriptive statistics:")
    print(descriptive_stats)


# In[6]:


def display_skewness(data):
    # Display skewness for each numerical column
    skewness = data.skew()
    print("Skewness for each column:")
    print(skewness)


# In[7]:


def display_kurtosis(data):
    # Display kurtosis for each numerical column
    kurtosis_values = data.kurtosis()
    print("Kurtosis for each column:")
    print(kurtosis_values)


# In[8]:


def plot_numerical_feature_histograms(data, numerical_features):
    # Plot histograms for each numerical feature
    plt.figure(figsize=(12, 10))
    data[numerical_features].hist(bins=20, edgecolor='black', grid=False, layout=(3, 3), figsize=(12, 10), color='skyblue')
    plt.suptitle('Distribution of Numerical Features', fontsize=16)
    plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust layout for title
    plt.show()


# In[9]:


def plot_boxplots_numerical_features(data, numerical_features):
    # Plot individual boxplots for each numerical feature
    plt.figure(figsize=(12, 15))
    for i, feature in enumerate(numerical_features, 1):
        plt.subplot(3, 3, i)
        sns.boxplot(x=data[feature], palette='pastel')
        plt.title(f'Boxplot of {feature.capitalize()}', fontsize=12)
        plt.xlabel(feature.capitalize(), fontsize=10)
        plt.ylabel('Values', fontsize=10)
        plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility

    plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust layout for title
    plt.show()


# In[10]:


def plot_count_plots_categorical_features(data, categorical_features):
    # Plot individual count plots for each categorical feature
    plt.figure(figsize=(12, 10))
    for i, feature in enumerate(categorical_features, 1):
        plt.subplot(2, 3, i)
        sns.countplot(x=feature, data=data, palette='pastel')
        plt.title(f'Count Plot of {feature.capitalize()}', fontsize=12)
        plt.xlabel(feature.capitalize(), fontsize=10)
        plt.ylabel('Count', fontsize=10)

    plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust layout for title
    plt.show()


# In[11]:


def plot_correlation_matrix(data):
    # Compute the correlation matrix
    correlation_matrix = data.corr()

    # Plot the correlation matrix using a heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
    plt.title('Correlation Matrix', fontsize=16)
    plt.show()


# In[12]:


def create_scatter_facetgrid(data):
    # List of categorical features
    categorical_features = ['anaemia', 'diabetes', 'high_blood_pressure', 'gender', 'smoking', 'DEATH_EVENT']

    # List of numerical features
    numerical_features = ['age', 'creatinine_phosphokinase', 'ejection_fraction', 'platelets', 'serum_creatinine', 'serum_sodium', 'time']

    # Create a FacetGrid for different categorical features against numerical features
    g = sns.FacetGrid(data, col="DEATH_EVENT", row="smoking", margin_titles=True, height=4, palette="pastel")
    g.map(plt.scatter, "age", "serum_creatinine", edgecolor="white", alpha=0.7)
    g.set_axis_labels("Age", "Serum Creatinine")
    g.set_titles(col_template="{col_name} Death Event", row_template="{row_name} Smoking")
    g.set(xlim=(0, 100), ylim=(0, 10), xticks=[0, 20, 40, 60, 80, 100], yticks=[0, 2, 4, 6, 8, 10])

    # Add a legend for the 'DEATH_EVENT' column
    g.add_legend()

    # Adjust the layout for better spacing
    g.fig.subplots_adjust(wspace=.02, hspace=.02)

    # Set a stylish background color
    g.fig.set_facecolor("#f5f5f5")

    plt.show()


# In[13]:


def create_stacked_bar_plot(data, x_feature, hue_feature):
    # List of categorical features
    categorical_features = ['anaemia', 'diabetes', 'high_blood_pressure', 'gender', 'smoking', 'DEATH_EVENT']

    # Create a stacked bar plot for the relationship between two categorical features
    plt.figure(figsize=(12, 8))
    sns.countplot(x=x_feature, hue=hue_feature, data=data, palette='pastel')

    # Add labels and title
    plt.title(f'Relationship between {x_feature.capitalize()} and {hue_feature.capitalize()}', fontsize=16)
    plt.xlabel(x_feature.capitalize(), fontsize=14)
    plt.ylabel('Count', fontsize=14)

    # Add legend for 'hue_feature' categories
    plt.legend(title=hue_feature.capitalize(), title_fontsize='12', loc='upper right')

    plt.show()


# In[14]:


def create_stacked_bar_plot_multiple_factors(data, x_feature, hue1_feature, hue2_feature):
    # List of categorical features
    categorical_features = ['anaemia', 'diabetes', 'high_blood_pressure', 'gender', 'smoking', 'DEATH_EVENT']

    # Create a stacked bar plot for the relationship between two categorical features
    plt.figure(figsize=(12, 8))
    sns.countplot(x=x_feature, hue=hue1_feature, data=data, palette='pastel', hue_order=[1, 0])
    sns.countplot(x=x_feature, hue=hue2_feature, data=data, palette='muted', hue_order=[1, 0], alpha=0.8)

    # Add labels and title
    plt.title(f'Relationship between {hue1_feature.capitalize()}, {hue2_feature.capitalize()}, and {x_feature.capitalize()}', fontsize=16)
    plt.xlabel(x_feature.capitalize(), fontsize=14)
    plt.ylabel('Count', fontsize=14)

    # Add legend
    plt.legend(title='Factor', title_fontsize='12', loc='upper right', labels=[hue1_feature.capitalize(), hue2_feature.capitalize()])

    plt.show()


# In[15]:


def create_stacked_bar_plot_multiple_factors(data, x_feature, hue1_feature, hue2_feature):
    # List of categorical features
    categorical_features = ['anaemia', 'diabetes', 'high_blood_pressure', 'gender', 'smoking', 'DEATH_EVENT']

    # Create a stacked bar plot for the relationship between two categorical features
    plt.figure(figsize=(12, 8))
    sns.countplot(x=x_feature, hue=hue1_feature, data=data, palette='pastel', hue_order=[1, 0])
    sns.countplot(x=x_feature, hue=hue2_feature, data=data, palette='muted', hue_order=[1, 0], alpha=0.8)

    # Add labels and title
    plt.title(f'Relationship between {hue1_feature.capitalize()}, {hue2_feature.capitalize()}, and {x_feature.capitalize()}', fontsize=16)
    plt.xlabel(x_feature.capitalize(), fontsize=14)
    plt.ylabel('Count', fontsize=14)

    # Add legend
    plt.legend(title='Factor', title_fontsize='12', loc='upper right', labels=[hue1_feature.capitalize(), hue2_feature.capitalize()])

    plt.show()


# In[16]:


def plot_survival_bar(df):
    # Separate data into groups based on 'DEATH_EVENT'
    survived = df[df['DEATH_EVENT'] == 0]
    died = df[df['DEATH_EVENT'] == 1]

    # Get all possible labels
    labels = df['DEATH_EVENT'].unique()

    # Calculate the number of observations for each group
    heights = [len(died), len(survived)]

    # Create a bar plot
    plt.bar(labels, heights, color='grey')
    plt.xticks(labels, ['Died', 'Survived'])
    plt.ylabel("# of observations")
    plt.title('Survival Analysis')
    plt.show()


# In[17]:


def plot_anaemia_bar(df):
    # Separate data into groups based on 'DEATH_EVENT'
    no_anaemia = df[df['anaemia'] == 0]
    anaemia = df[df['anaemia'] == 1]

    # Get all possible labels
    labels = df['anaemia'].unique()

    # Calculate the number of observations for each group
    heights = [len(anaemia), len(no_anaemia)]

    # Create a bar plot
    plt.bar(labels, heights, color='grey')
    plt.xticks(labels, ['Had Anaemia', 'Does not have Anaemia'])
    plt.ylabel("# of observations")
    plt.title('Anaemia Analysis')
    plt.show()


# In[18]:


def hbp(df):
    # Separate data into groups based on 'DEATH_EVENT'
    no_hbp = df[df['high_blood_pressure'] == 0]
    hbp = df[df['high_blood_pressure'] == 1]

    # Get all possible labels
    labels = df['high_blood_pressure'].unique()

    # Calculate the number of observations for each group
    heights = [len(hbp), len(no_hbp)]

    # Create a bar plot
    plt.bar(labels, heights, color='grey')
    plt.xticks(labels, ['HBP', 'No HBP'])
    plt.ylabel("# of observations")
    plt.title('High Blood Pressure Analysis')
    plt.show()


# In[ ]:




