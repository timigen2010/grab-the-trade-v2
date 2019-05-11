from db.models import Article, Key

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords

from django.utils import timezone


class KeyManager:
    @staticmethod
    def get_unused_key():
        latest_articles = Article.objects.order_by('-date_added')[:100]

        articles_texts = [a.text for a in latest_articles]

        tfidf_vectorizer = TfidfVectorizer(max_features=4, stop_words=stopwords.words('russian'))
        tfidf_vectorizer.fit_transform(articles_texts)

        key = " ".join(tfidf_vectorizer.get_feature_names()) + " новости"

        rk, created = Key.objects.get_or_create(key=key)
        if not created and abs((rk.date_used - timezone.now()).days) > 90:
            rk.date_used = timezone.now()
            rk.save()
        elif not created:
            rk = False

        return rk
