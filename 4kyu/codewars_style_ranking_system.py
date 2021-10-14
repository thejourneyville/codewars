"""
Write a class called User that is used to calculate the amount that a user will progress through a 
ranking system similar to the one Codewars uses.

Business Rules:
A user starts at rank -8 and can progress all the way to 8.
There is no 0 (zero) rank. The next rank after -1 is 1.
Users will complete activities. These activities also have ranks.
Each time the user completes a ranked activity the users rank progress is updated based off of the activity's rank
The progress earned from the completed activity is relative to what the user's current rank is compared to the rank of the activity
A user's rank progress starts off at zero, each time the progress reaches 100 the user's rank is upgraded to the next level
Any remaining progress earned while in the previous rank will be applied towards the next rank's progress 
(we don't throw any progress away). The exception is if there is no other rank left to progress towards 
(Once you reach rank 8 there is no more progression).
A user cannot progress beyond rank 8.
The only acceptable range of rank values is -8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8. Any other value should raise an error.

The progress is scored like so:
Completing an activity that is ranked the same as that of the user's will be worth 3 points
Completing an activity that is ranked one ranking lower than the user's will be worth 1 point
Any activities completed that are ranking 2 levels or more lower than the user's ranking will be ignored
Completing an activity ranked higher than the current user's rank will accelerate the rank progression. 
The greater the difference between rankings the more the progression will be increased. 
The formula is 10 * d * d where d equals the difference in ranking between the activity and the user.

Logic Examples:
If a user ranked -8 completes an activity ranked -7 they will receive 10 progress
If a user ranked -8 completes an activity ranked -6 they will receive 40 progress
If a user ranked -8 completes an activity ranked -5 they will receive 90 progress
If a user ranked -8 completes an activity ranked -4 they will receive 160 progress, resulting i
n the user being upgraded to rank -7 and having earned 60 progress towards their next rank
If a user ranked -1 completes an activity ranked 1 they will receive 10 progress (remember, zero rank is ignored)

Code Usage Examples:
user = User()
user.rank # => -8
user.progress # => 0
user.inc_progress(-7)
user.progress # => 10
user.inc_progress(-5) # will add 90 progress
user.progress # => 0 # progress is now zero
user.rank # => -7 # rank was upgraded to -7
"""

class User:
    def __init__(self):
        self.ranks = (-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8)
        self.rank = -8
        self.progress = 0
        self.progress_earned = 0

    # inc_progress passes the completed kata rank
    def inc_progress(self, kata_rank):
        
        if -8 > kata_rank > 8 or not kata_rank:
            raise Exception("invalid kata ranking")
            return -1
        
        # finding difference of rank of user and completed kata
        user_rank_idx = self.ranks.index(self.rank)
        kata_rank_idx = self.ranks.index(kata_rank)
        difference_in_rank_idx = abs(user_rank_idx - kata_rank_idx)

        
        # higher-ranked kata completed (formula):
        if difference_in_rank_idx:
            if self.rank < kata_rank:
                self.progress_earned = 10 * difference_in_rank_idx * difference_in_rank_idx
            else:
                if difference_in_rank_idx == 1:
                    self.progress_earned = 1
                else:
                    self.progress_earned = 0
        else:
            self.progress_earned = 3

        # tallying previous and earned progress
        current_total_progress = self.progress + self.progress_earned

        # rank_promotion: number of rank advancements
        # progress_carry_over: remainder of progress to be carried over
        rank_promotion, progress_carry_over = divmod(current_total_progress, 100)

        try:
            self.rank = self.ranks[user_rank_idx + rank_promotion]
        except IndexError:
            if user_rank_idx + rank_promotion >= len(self.ranks):
                self.rank = 8
        
        if self.rank == 8:
            self.progress = 0
        else:
            self.progress = progress_carry_over


# testing below
user = User()
print(user.progress)
print(user.rank)

user.inc_progress(-7)
print(user.progress)
print(user.rank)

user.inc_progress(-5)
print(user.progress)
print(user.rank)
