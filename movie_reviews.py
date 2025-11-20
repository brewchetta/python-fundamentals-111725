from datetime import date

class MovieReview:

	def __init__(self, movie_title, reviewer_name, score, date_reviewed):
		self.movie_title = movie_title
		self.reviewer_name = reviewer_name
		self.score = score
		self.date_reviewed = date_reviewed

	# Create a class `MovieReview` which has required attributes `movie_title:str`, `reviewer_name:str`, `score:int`, `date_reviewed:datetime.date`.
		# You may need to look up how to use `datetime.date` (hint: you'll need `from datetime import date`)`

	def pretty_print(self):
		return f"{self.movie_title} review by {self.reviewer_name} on {self.date_reviewed}: {self.score} / 5"

	# Create an instance method `pretty_print()` which prints the review like so: `"<movie_title> review by <reviewer_name> on <date_reviewed>: <score> / 5 stars"`.
		# Example: `land_before_time.pretty_print()` >>> `"Land Before Time review by Fred Flintstone on 2014-4-12: 5/5 stars"`

	def increase_score(self):
		if self.score < 5:
			self.score += 1
		return self.score

	# Create an instance method `increase_score()` which increases that movie's score by 1 but not above 5.

	def update_review(self, new_score, new_reviewer=None):
		self.score = new_score
		self.date_reviewed = date.today()
		if new_reviewer is not None:
			self.reviewer_name = new_reviewer

	# Create an instance method `update_review()`. This accepts an argument of a `new_score` and optionally a `new_reviewer`. This updates the `score` and sets the `date_reviewed` to today.  If `new_reviewer` was passed this will also update the `reviewer_name` and if not it will retain the previous `reviewer_name`.
	# Example: `land_before_time.update_review(4)` # score changed to `4`, date becomes today, reviewer is still `"Fred Flinstone"`
	# Example: `land_before_time.update_review(5, "Littlefoot")` # score changed to `5`, date becomes today, reviewer becomes `"Littlefoot"`

	@classmethod
	def review_bomb(cls, movie_title, num_reviews):

		new_list = []

		for _ in range(num_reviews):

			new_review = cls(reviewer_name="Statler & Waldorf", movie_title=movie_title, date_reviewed=date.today(), score=1)

			new_list.append(new_review)

		return new_list

	# Create a class method `review_bomb()` which accepts a `movie_title` and `num_reviews`. This generates a review `num_reviews` times for the `movie_title` each with a `score` of 1, a `reviewer_name` of `Statler & Waldorf`, and a `date_reviewed` of today. Return all instances in a list.
	# Example: `MovieReview.review_bomb("Plan 9 From Outer Space", 10)` >>> creates 10 reviews for "Plan 9 From Outer Space"