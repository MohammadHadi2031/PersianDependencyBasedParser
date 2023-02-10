from bert_embedding import BertEmbedding

lines = []
with open('/content/bert-utf8.txt', 'r', encoding='utf-8') as f:
  lines.append(f.readline().strip())

b_sentences = []
for line in lines:
  b_sentences.append(line.split())

b_sentences

bert_embedding = BertEmbedding()
result = bert_embedding(lines)
print(result)
