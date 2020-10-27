def ChordID(chordNotes):

  # Takes in an array called "chordNotes" and returns an array of possible
  # chord names associated with the pitches defined in chordNotes.
  # NOTE: Current version ignores inversions.
  #
  # e.g. ChordID(['C','E','A']) returns ['C Maj6', 'A min']
  #
  # Evan Czako, 10.27.2020.

  notesSharps = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
  notesFlats = ['A','Bb','B','C','Db','D','Eb','E','F','Gb','G','Ab']

  possibleChords = [];

  chordNotesIndices = set()
  for note in chordNotes:
    if note in notesSharps:
      chordNotesIndices.add(notesSharps.index(note))
    elif note in notesFlats:
      chordNotesIndices.add(notesFlats.index(note))

  checkList = list(chordNotesIndices)


  ### Power Chord ###
  powerChordSet = {0,7}

  ### Check Power Chords ###
  for k in range(0,12):
    
    tempSet = set([(x+k)%12 for x in checkList])

    if tempSet == powerChordSet:
      possibleChords.append(notesSharps[(0-k)%12]+" PowerChord")
      break  


  ### Major Chords ###
  majSet = {0,4}
  maj7Set = {0, 4, 11}
  maj9Set = {0, 4, 11, 2}
  maj11Set = {0, 4, 11, 2, 5}
  maj13Set = {0, 4, 11, 2, 5, 9}
  majAdd9Set = {0, 4, 2}
  majAdd11Set = {0, 4, 5}
  maj6Set = {0, 4, 9}
  majAdd9Add11Set = {0, 4, 2, 5}
  sixNineSet = {0, 4, 2, 9}
  majAdd11Add13Set = {0, 4, 5, 9}
  majAdd9Add11Add13Set = {0, 4, 2, 5, 9}
  maj9Add13Set = {0, 4, 11, 2, 9}
  

  ### Check major chords ###
  for k in range(0,12):
    
    tempSet = set([(x+k)%12 for x in checkList])
    tempSet.discard(7)

    if tempSet == majSet:
      possibleChords.append(notesSharps[(0-k)%12]+" Maj")
    elif tempSet == maj7Set:
      possibleChords.append(notesSharps[(0-k)%12]+" Maj7")
    elif tempSet == maj9Set:
      possibleChords.append(notesSharps[(0-k)%12]+" Maj9")
    elif tempSet == maj11Set:
      possibleChords.append(notesSharps[(0-k)%12]+" Maj11")
    elif tempSet == maj13Set:
      possibleChords.append(notesSharps[(0-k)%12]+" Maj13")
    elif tempSet == majAdd9Set:
      possibleChords.append(notesSharps[(0-k)%12]+" MajAdd9")
    elif tempSet == majAdd11Set:
      possibleChords.append(notesSharps[(0-k)%12]+" MajAdd11")
    elif tempSet == maj6Set:
      possibleChords.append(notesSharps[(0-k)%12]+" Maj6")
    elif tempSet == majAdd9Add11Set:
      possibleChords.append(notesSharps[(0-k)%12]+" MajAdd9Add11")    
    elif tempSet == sixNineSet:
      possibleChords.append(notesSharps[(0-k)%12]+" Maj69")
    elif tempSet == majAdd11Add13Set:
      possibleChords.append(notesSharps[(0-k)%12]+" MajAdd11Add13")
    elif tempSet == majAdd9Add11Add13Set:
      possibleChords.append(notesSharps[(0-k)%12]+" MajAdd9Add11Add13")
    elif tempSet == maj9Add13Set:
      possibleChords.append(notesSharps[(0-k)%12]+" Maj9Add13")




  ### Minor Chords ###
  minSet = {0,3}
  min6Set = {0, 3, 9}
  min7Set = {0, 3, 10}
  min9Set = {0, 3, 10, 2}
  min11Set = {0, 3, 10, 2, 5}
  min13Set = {0, 3, 10, 2, 5, 9}
  minAdd9Set = {0, 3, 2}
  minAdd11Set = {0, 3, 5}
  minAdd9Add11Set = {0, 3, 2, 5}
  min6Add9Set = {0, 3, 2, 9}
  minAdd9Add11Add13Set = {0, 3, 2, 5, 9}
  min7Add11Set = {0, 3, 10, 5}


  ### Check minor chords ###
  for k in range(0,12):
    
    tempSet = set([(x+k)%12 for x in checkList])
    tempSet.discard(7)

    if tempSet == minSet:
      possibleChords.append(notesSharps[(0-k)%12]+" min")
    elif tempSet == min6Set:
      possibleChords.append(notesSharps[(0-k)%12]+" min6")
    elif tempSet == min7Set:
      possibleChords.append(notesSharps[(0-k)%12]+" min7")
    elif tempSet == min9Set:
      possibleChords.append(notesSharps[(0-k)%12]+" min9")
    elif tempSet == min11Set:
      possibleChords.append(notesSharps[(0-k)%12]+" min11")   
    elif tempSet == min13Set:
      possibleChords.append(notesSharps[(0-k)%12]+" min13")
    elif tempSet == minAdd9Set:
      possibleChords.append(notesSharps[(0-k)%12]+" minAdd9")
    elif tempSet == minAdd11Set:
      possibleChords.append(notesSharps[(0-k)%12]+" minAdd11")
    elif tempSet == minAdd9Add11Set:
      possibleChords.append(notesSharps[(0-k)%12]+" minAdd9Add11")
    elif tempSet == min6Add9Set:
      possibleChords.append(notesSharps[(0-k)%12]+" min6Add9")
    elif tempSet == minAdd9Add11Add13Set:
      possibleChords.append(notesSharps[(0-k)%12]+" minAdd9Add11Add13")
    elif tempSet == min7Add11Set:
      possibleChords.append(notesSharps[(0-k)%12]+" min7Add11")




### Dominant Chords ###
  dom7Set = {0, 4, 10}
  dom9Set = {0, 4, 10, 2}
  dom11Set = {0, 4, 10, 2, 5}
  dom13Set = {0, 4, 10, 2, 5, 9}
  dom7b9Set = {0, 4, 10, 1}
  dom7Sharp9Set = {0, 4, 10, 3}
  dom7b5Set = {0, 4, 10, 6}
  dom7b13Set = {0, 4, 10, 8}
  dom9b5Set = {0, 4, 10, 2, 6}
  alteredSet = {0, 4, 10, 1, 3, 6, 8}


  ### Check dominant chords ###
  for k in range(0,12):
    
    tempSet = set([(x+k)%12 for x in checkList])
    tempSet.discard(7)

    if tempSet == dom7Set:
      possibleChords.append(notesSharps[(0-k)%12]+" 7")
    if tempSet == dom9Set:
      possibleChords.append(notesSharps[(0-k)%12]+" 9")
    if tempSet == dom11Set:
      possibleChords.append(notesSharps[(0-k)%12]+" 11")
    if tempSet == dom13Set:
      possibleChords.append(notesSharps[(0-k)%12]+" 13")
    if tempSet == dom7b9Set:
      possibleChords.append(notesSharps[(0-k)%12]+" 7b9")
    if tempSet == dom7Sharp9Set:
      possibleChords.append(notesSharps[(0-k)%12]+" 7#9")
    if tempSet == dom7b5Set:
      possibleChords.append(notesSharps[(0-k)%12]+" 7b5")
    if tempSet == dom7b13Set:
      possibleChords.append(notesSharps[(0-k)%12]+" 7b13")
    if tempSet == dom9b5Set:
      possibleChords.append(notesSharps[(0-k)%12]+" 9b5")
    if tempSet == alteredSet:
      possibleChords.append(notesSharps[(0-k)%12]+" Alt")



### Sus Chords ###
  sus4Set = {0, 5}
  sus2Set = {0, 2}
  sus2sus4Set = {0, 2, 5}
  dom7sus4Set = {0, 5, 10}
  dom7sus2Set = {0, 2, 10}
  dom9Sus4Set = {0, 5, 10, 2}
  dom7b9SusSet = {0, 5, 10, 1}
  sus13Set = {0, 10, 2, 5, 9}
  sus13b9Set = {0, 10, 1, 5, 9}
  sus4b9Set = {0, 5, 1}



  ### Check sus chords ###
  for k in range(0,12):
    
    tempSet = set([(x+k)%12 for x in checkList])
    tempSet.discard(7)

    if tempSet == sus4Set:
      possibleChords.append(notesSharps[(0-k)%12]+" sus4")
    if tempSet == sus2Set:
      possibleChords.append(notesSharps[(0-k)%12]+" sus2")
    if tempSet == sus2sus4Set:
      possibleChords.append(notesSharps[(0-k)%12]+" sus2sus4")      
    if tempSet == dom7sus4Set:
      possibleChords.append(notesSharps[(0-k)%12]+" 7sus4")
    if tempSet == dom7sus2Set:
      possibleChords.append(notesSharps[(0-k)%12]+" 7sus2")
    if tempSet == dom9Sus4Set:
      possibleChords.append(notesSharps[(0-k)%12]+" 9sus4")
    if tempSet == dom7b9SusSet:
      possibleChords.append(notesSharps[(0-k)%12]+" 7b9sus")
    if tempSet == sus13Set:
      possibleChords.append(notesSharps[(0-k)%12]+" sus13")
    if tempSet == sus13b9Set:
      possibleChords.append(notesSharps[(0-k)%12]+" sus13b9")
    if tempSet == sus4b9Set:
      possibleChords.append(notesSharps[(0-k)%12]+" sus4b9")



### Dim Chords ###
  dimSet = {0, 3, 6}
  halfDimSet = {0, 3, 6, 10}
  fullDimSet = {0, 3, 6, 9}


  ### Check dim chords ###
  for k in range(0,12):
    
    tempSet = set([(x+k)%12 for x in checkList])

    if tempSet == dimSet:
      possibleChords.append(notesSharps[(0-k)%12]+" dim")
    if tempSet == halfDimSet:
      possibleChords.append(notesSharps[(0-k)%12]+" halfDim")
    if tempSet == fullDimSet:
      possibleChords.append(notesSharps[(0-k)%12]+" fullDim")




### MinMaj Chords ###
  minMajSet = {0, 3, 11}
  minMaj9Set = {0, 3, 11, 2}
  minMaj9b13Set = {0, 3, 11, 2, 8}


  ### Check minMaj chords ###
  for k in range(0,12):
    
    tempSet = set([(x+k)%12 for x in checkList])
    tempSet.discard(7)

    if tempSet == minMajSet:
      possibleChords.append(notesSharps[(0-k)%12]+" minMaj")
    if tempSet == minMaj9Set:
      possibleChords.append(notesSharps[(0-k)%12]+" minMaj9")
    if tempSet == minMaj9b13Set:
      possibleChords.append(notesSharps[(0-k)%12]+" minMaj9b13")



### Aug Chords ###
  AugSet = {0, 4, 8}
  Aug7Set = {0, 4, 8, 10}
  AugMaj7Set = {0, 4, 8, 11}


  ### Check aug chords ###
  for k in range(0,12):
    
    tempSet = set([(x+k)%12 for x in checkList])

    if tempSet == AugSet:
      possibleChords.append(notesSharps[(0-k)%12]+" Aug")
    if tempSet == Aug7Set:
      possibleChords.append(notesSharps[(0-k)%12]+" Aug7")
    if tempSet == AugMaj7Set:
      possibleChords.append(notesSharps[(0-k)%12]+" AugMaj7")



### b5 and #11 Chords ###
  Majb5Set = {0, 4, 6}
  Maj7b5Set = {0, 4, 6, 11}
  Maj9b5Set = {0, 4, 6, 11, 2}
  maj7AddSharp11Set = {0, 4, 7, 11, 6}
  maj9AddSharp11Set = {0, 4, 7, 11, 2, 6}
  maj13Sharp11Set = {0, 4, 7, 11, 2, 6, 9}
  majAddSharp11Set = {0, 4, 7, 6}

  ### Check b5 and #11 chords ###
  for k in range(0,12):
    
    tempSet = set([(x+k)%12 for x in checkList])

    if tempSet == Majb5Set:
      possibleChords.append(notesSharps[(0-k)%12]+" Majb5")
    if tempSet == Maj7b5Set:
      possibleChords.append(notesSharps[(0-k)%12]+" Maj7b5")
    if tempSet == Maj9b5Set:
      possibleChords.append(notesSharps[(0-k)%12]+" Maj9b5")      
    elif tempSet == maj7AddSharp11Set:
      possibleChords.append(notesSharps[(0-k)%12]+" Maj7Add#11")
    elif tempSet == maj9AddSharp11Set:
      possibleChords.append(notesSharps[(0-k)%12]+" Maj9Add#11")
    elif tempSet == maj13Sharp11Set:
      possibleChords.append(notesSharps[(0-k)%12]+" Maj13#11")
    elif tempSet == majAddSharp11Set:
      possibleChords.append(notesSharps[(0-k)%12]+" MajAdd#11")





  return possibleChords