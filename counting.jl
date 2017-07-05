#A deck with 52 cards - 4 suites and 13 ranks - A,2,...,10,J,Q,K
deck = [(suite,r) for suite in ["♡","♢", "♣", "♠"]  for r in range(1,13)]

function simulate_pair(n = 100, verbose=false)
    pairs = 0
    for i in 1:n
        hand = shuffle(deck)[1:2]
        if length(unique([r for (s,r) in hand])) == 1
                if verbose
                    println(hand)
                end
                pairs += 1
        end
    end
    100.*pairs/n
end
good_pairs(len_deck = 52) = (len_deck*3)/2
all_pairs(len_deck = 52) = binomial(len_deck, 2)

function simulate_disjoint_triplet(n = 100, verbose=false)
    triplets = 0
    for i in 1:n
        hand = shuffle(deck)[1:3]
        if length(unique([r for (s,r) in hand])) == 3 
                if verbose
                    println(hand)
                end
                triplets += 1
        end
    end
    100.*triplets/n
end
disjoint_triplets(len_deck = 52) = (len_deck*(len_deck-4)*(len_deck-8))/factorial(3)
all_triplets(len_deck = 52) = binomial(len_deck, 3)


function simulate_one_pair_hand(n = 100, verbose=false)
    pairs = 0
    for i in 1:n
        hand = shuffle(deck)[1:5]
        if length(unique([r for (s,r) in hand])) == 4
                if verbose
                    println(hand)
                end
                pairs += 1
        end
    end
    100.*pairs/n
end
prob_one_pair_hand = 100.* good_pairs(52) * disjoint_triplets(48) / binomial(52,5)


