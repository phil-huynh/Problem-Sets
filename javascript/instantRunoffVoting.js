/* Your task is to implement a function that calculates an election winner from a list of voter selections using an Instant Runoff Voting algorithm. If you haven't heard of IRV, here's a basic overview (slightly altered for this kata):

    Each voter selects several candidates in order of preference.

    The votes are tallied from the each voter's first choice.

    If the first-place candidate has more than half the total votes, they win.

    Otherwise, find the candidate who got the least votes and remove them from each person's voting list.

    In case of a tie for least, remove all of the tying candidates.

    In case of a complete tie between every candidate, return nil(Ruby)/None(Python)/undefined(JS).

    Start over.

    Continue until somebody has more than half the votes; they are the winner.

Your function will be given a list of voter ballots; each ballot will be a list of candidates (symbols) in descending order of preference. You should return the symbol corresponding to the winning candidate. See the default test for an example! */

function runoff(voters){
  const total = voters.length
  let tally = {}
  for (let candidate of voters[0]) {
    tally[candidate] = 0
  }
  let count = voters.map((ballot) => ballot[0])
  count.forEach((vote) => {
    tally[vote]++
  })
  let votes = []
  for(const key in tally) {
    votes.push(tally[key])
    if (tally[key] > total/2) {
      return key
    }
  }
  if(votes.every(vote => vote===votes[0])) {
    return undefined
  }
  let lowest = votes.sort((a, b) => a - b)
  ballots = voters.map(ballot => ballot.filter(person => tally[person] !== lowest[0]))
  return runoff(ballots)
}