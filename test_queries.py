import queries as q

def test():
    assert q.get_candidate_queries('n','CandidateData/','keywords') == ['bjr']
