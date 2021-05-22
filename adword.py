from math import exp
"""
Author: Victor Jørgensen"
Simple program to run Greedy Algorithm, Balance Algorithm and General Balance Algorithm to solve adword problem.
"""


class Advertiser:
    """
    Represents a company advertising ads

    params:
    id = identifier for advertiser. Preferably int.
    budget = Initial budget for advertiser
    """

    def __init__(self, id, budget):
        self.id = id
        self.budget = budget
        self.amount_spent = 0

    def __str__(self):
        return "Advertiser: a{}, Budget: {}, Amount spent: {}, Bid: {}".format(self.id, self.budget, self.amount_spent, self.bid)


class Query:
    """
    Represents a query for adverds. Related to a list of advertisers who bid for query word.

    params:
    query = The query the advertisers bid for. Can be either q1,q2,q3... etc or "cars", "brakes",...
    advertisers = An array of the advertisers with a bid for this query. E.g.: [a1,a2,a3]
    bids = An array of the bids for each advertiser. Must be indexed the same as the related advertiser!
    """

    def __init__(self, query, advertisers, bids):
        self.advertisers = advertisers
        self.bids = bids
        self.query = query

    def score(self, budget, amount_spent, bid):
        """
        Calculates scored used in GBA
        """
        if amount_spent == 0 or budget == 0:
            return bid * (1 - exp(-1))
        return bid * (1 - exp(-1 - amount_spent/budget))

    def get_max_score(self):
        """
        Return advertiser with highest score
        """
        for index, advertiser in enumerate(self.advertisers):
            advertiser.score = self.score(
                advertiser.budget, advertiser.amount_spent, self.bids[index])
            advertiser.bid = self.bids[index]
        winner = None
        for advertiser in self.advertisers:
            if winner is None:
                winner = advertiser
            else:
                if advertiser.score > winner.score:
                    winner = advertiser
        return winner

    def get_selected_advertiser(self):
        while len(self.advertisers) > 0:
            winner = self.get_max_score()
            if winner is not None and winner.budget >= winner.bid:
                winner.budget -= winner.bid
                winner.amount_spent += winner.bid

                return (winner)
            else:
                self.advertisers.remove(winner)
        return "No advertiser with sufficient funds left"

    def get_greedy(self):
        """
        Used in Greedy Algorithm approach to adword problem. 
        Return advertiser with a bid for current query. Tie break by advertiser ID.
        """
        return self.advertisers[0]

    def get_highest_budget(self):
        """
        Used in Balance Algorithm.
        Returns advertiser with highest unspent budget.
        """
        winner = None
        for advertiser in self.advertisers:
            if winner is None:
                winner = advertiser
            else:
                if winner.budget < advertiser.budget:
                    winner = advertiser
        return winner


def greedy_algorithm(queries, query_timeline):
    """
    Simple implementation of Greedy Algorithm approach to adword problem. 
    Assumptions:
    - All bids are 1 or 0
    - Every advert has the same expected revenue
    - Initialized budgets and bids are integers

    params:
    queries = List of intialized query objects
    query_timeline = Ordered list representing timeline of queries
    """
    revenue = 0

    for q in query_timeline:

        query = queries[q-1]

        # Run function to add bid attribute to advertiser. We dont use the score in greedy.
        query.get_max_score()

        winner = query.get_greedy()
        print(winner, "Revenue: ", revenue)
        if isinstance(winner, Advertiser) and winner.budget >= 0:
            revenue += 1

    print("Revenue: {}".format(revenue))


def balance_algorithm(queries, query_timeline):
    """"
    Implementation of General Balance Algorithm to solve adword problem.
    Prints selected advertiser with budget, bid, amount spent and revenue so far for each query, or message if none. 

    params:
    queries = List of intialized query objects
    query_timeline = Ordered list representing timeline of queries
    """
    revenue = 0
    for q in query_timeline:
        query = queries[q-1]

        # Run function to add bid attribute to advertiser. We dont use the score in greedy.
        query.get_max_score()

        winner = query.get_highest_budget()
        if isinstance(winner, Advertiser) and winner.budget >= winner.bid:
            revenue += winner.bid
            winner.amount_spent += winner.bid
            winner.budget -= winner.bid
            print(winner, "Revenue: ", revenue)
        else:
            print("No advertisers with sufficient funds left")

    print("Revenue: {}".format(revenue))


def general_balance_algorithm(queries, query_timeline):
    """
    Implementation of General Balance Algorithm to solve adword problem.
    Prints selected advertiser with budget, bid, amount spent and revenue so far for each query, or message if none. 

    params:
    queries = List of intialized query objects
    query_timeline = Ordered list representing timeline of queries
    """
    revenue = 0
    for q in query_timeline:
        winner = queries[q-1].get_selected_advertiser()
        print(winner, "Revenue: ", revenue)
        if isinstance(winner, Advertiser):
            revenue += winner.bid

    print("Revenue: {}".format(revenue))


if __name__ == "__main__":
    # Init advertisers and add them to array.
    a1 = Advertiser(1, 3)
    a2 = Advertiser(2, 1)
    a3 = Advertiser(3, 1)
    a4 = Advertiser(4, 2)
    advertisers = [a1, a2, a3, a4]

    # Init queries with advertisers and bids, add to list
    q1 = Query(1, [a1, a4], [0.5, 0.75])
    q2 = Query(2, [a2, a3], [0.5, 0.5])
    q3 = Query(3, [a1], [1])
    q4 = Query(4, [a3], [1])
    queries = [q1, q2, q3, q4]

    # Timeline of the queries
    query_timeline = [1, 2, 3, 4, 3, 3, 2, 4]

    # Prompt user for which algorithm to run
    prompt = input(
        "1. Greedy Algorithm\n2. Balance Algorithm \n3. General Balance Algorithm\n\n")
    if prompt == "1":
        # Run greedy algorithm
        greedy_algorithm(queries, query_timeline)
    elif prompt == "2":
        # Run balance algorithm
        balance_algorithm(queries, query_timeline)
    elif prompt == "3":
        # Run general balance algorithm
        general_balance_algorithm(queries, query_timeline)
