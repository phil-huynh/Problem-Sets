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