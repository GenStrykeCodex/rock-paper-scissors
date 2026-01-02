""" Scores Module ---------------------- Handles scores saving and loading."""

# importing module
import os

# file to store the expenses
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
SCORES_FILE = os.path.join(DATA_DIR, "scores.txt")

# auto-create /data folder on first run
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

# defining list to store scores
user_score_list = []
comp_score_list = []
results_list = []

# load scores from the text file into list
def load_scores():

    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, 'r') as f:
            for line in f:
                line = line.strip()

                if line:  # Skip empty lines
                    # Split by comma [user_score, comp_score, user_win]
                    parts = line.split(',')

                    if len(parts) == 3:
                        # appends the list with values
                        user_score_list.append(parts[0])
                        comp_score_list.append(parts[1])
                        results_list.append(parts[2])


        print("Loaded all previous scores data from the file..\n")
    else:
        print("Unable to fetch previous scores data, starting a new file..\n")

# updating the scores from list to text file
def update_scores():

    with open(SCORES_FILE, 'w') as f:
        for user_score, comp_score, result in zip(user_score_list, comp_score_list, results_list):
            f.write(f"{user_score},{comp_score},{result}\n")

# updating the lists with new values
def update_lists(u_score, c_score, m_result):
    
    user_score_list.append(u_score)
    comp_score_list.append(c_score)
    results_list.append(m_result)

    # updating the file
    update_scores()

    print(f"\n✓ Score updated successfully!\n")

# display all scores saveed
def view_scores():

    if not user_score_list:
        print("\nNo data of scores available.\n")
        return
    
    print("\n" + "="*50)
    print(f"{'#':<5} {'Your Score':<13} {'Computer Score':<17} {'Result':<15}")
    print("="*50)

    for i, (u_score, c_score, m_result) in enumerate(zip(user_score_list, comp_score_list, results_list), 1):
        print(f"{i:<5} {u_score:<13} {c_score:<17} {m_result:<15}")

    print("="*50 + "\n")