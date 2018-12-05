from pattern.en import pluralize, singularize, comparative, superlative, conjugate, INFINITIVE, PRESENT, PAST, FUTURE
import spacy

# pip install pattern3

nlp = spacy.load('en_core_web_sm')

word_actions = {
	'NN': [pluralize],
	'NNP' : [pluralize],
	'NNS': [singularize],
	'NNPS': [singularize],
	'JJ': [comparative, superlative],
	'JJR': [superlative],
	'JJS': [comparative],
	'RB': [comparative, superlative],
	'RBR': [superlative],
	'RBS': [comparative]
}

def get_word_forms(word):
	return word

def get_all_word_forms(word_list = []):
	all_word_forms = []
	for word in word_list:
		all_word_forms.extend(get_word_forms(word))
	print(all_word_forms)
	return all_word_forms

	
if __name__ == '__main__':
	print('TESTING NOUN')
	word = 'Company'
	word_forms = get_word_forms(word)

	word = 'Counterparties'
	word_forms = get_word_forms(word)

	print('TESTING ADJECTIVE')
	word = 'Concerned'
	word_forms = get_word_forms(word)

	word = 'agreeable'
	word_forms = get_word_forms(word)

	print('TESTING VERBS')
	word = 'been'
	word_forms = get_word_forms(word)

	word = 'write'
	word_forms = get_word_forms(word)

