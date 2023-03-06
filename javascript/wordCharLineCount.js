function DocumentParser(reader)
{
  this.reader = reader;
  this.reset();
}

DocumentParser.prototype.reset = function()
{
  this.wordCount = 0;
  this.charCount = 0;
  this.lineCount = 0;
};

DocumentParser.prototype.parse = function()
{
  let text = ""
  let chunk = this.reader.getChunk()
  while (chunk) {
    text += chunk
    chunk = this.reader.getChunk()
  }
  if (text) {
    let lines = text.split('\n')
    this.lineCount += lines.length
    lines.forEach((line) => {
      if (line[0]) {
        let words = line.split(' ').map((word) => word.trim()).filter((word) => word)
        if(words[0]) {
          this.wordCount += words.length
        }
        this.charCount += line.length
      }
    })
  }
  text = this.reader.getChunk()

};