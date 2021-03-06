from pattern.en import pluralize, singularize, comparative, superlative, conjugate, INFINITIVE, PRESENT, PAST, FUTURE
import spacy

# pip install pattern3

nlp = spacy.load('en_core_web_sm')


def verb_present_conjugation(word):
	return conjugate(word, tense=PRESENT)

def verb_past_conjugation(word):
	return conjugate(word, tense=PAST)

def verb_future_conjugation(word):
	return conjugate(word, tense=FUTURE)

def verb_infinitive_conjugation(word):
	return conjugate(word, tense=INFINITIVE)

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
	'RBS': [comparative],
	'VB': [verb_present_conjugation, verb_past_conjugation, verb_future_conjugation, verb_infinitive_conjugation],
	'VBD': [verb_present_conjugation, verb_future_conjugation, verb_infinitive_conjugation],
	'VBG': [verb_present_conjugation, verb_past_conjugation, verb_future_conjugation, verb_infinitive_conjugation],
	'VBN': [verb_present_conjugation, verb_past_conjugation, verb_future_conjugation, verb_infinitive_conjugation],
	'VBP': [verb_present_conjugation, verb_past_conjugation, verb_future_conjugation, verb_infinitive_conjugation],
	'VBZ': [verb_present_conjugation, verb_past_conjugation, verb_future_conjugation, verb_infinitive_conjugation]
}

def get_word_forms(word):
	word_forms = [word]
	doc = nlp(unicode(word))
	if len(doc) > 1:
		return [word]
	word_tag = doc[0].tag_
	if word_tag is None:
		return word_forms
	if word_actions.get(word_tag):
		for action_name in word_actions.get(word_tag):
			word_form = action_name(word)
			if word_form is not None:
				word_forms.append(word_form)
	print(word, ': ', word_forms)
	return word_forms

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

