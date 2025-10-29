outcomes = [1, 2, 3, 4, 5, 6]                  
event_even = {2, 4, 6}
event_gt4 = {5, 6}
def probability(event, sample_space):
    return len(event) / len(sample_space)
p_even = probability(event_even, outcomes)
p_gt4 = probability(event_gt4, outcomes)
event_intersection = event_even.intersection(event_gt4)
p_intersection = probability(event_intersection, outcomes)
event_union = event_even.union(event_gt4)
p_union = probability(event_union, outcomes)
print("Sample Space:", outcomes)
print("Event Even:", event_even)
print("Event >4:", event_gt4)
print(f"P(Even) = {p_even:.2f}")
print(f"P(>4) = {p_gt4:.2f}")
print(f"P(Even ∩ >4) = {p_intersection:.2f}")
print(f"P(Even ∪ >4) = {p_union:.2f}")
