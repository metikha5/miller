#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, json, logging
from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase
from miller import helpers
from miller.models import Story, Author, Comment, Document


dir_path = os.path.dirname(os.path.realpath(__file__))

logger = logging.getLogger('console')

# python manage.py test miller.test.test_models_story.StoryTest
class StoryTest(TestCase):

  def setUp(self):
    self.user = User.objects.create_user(
        username='test-user-profile', 
        email='jacob@jacob', 
        password='top_secret')

    # document creation
    author = self.user.authorship.first()
    author.fullname=u'Jacob Jakobson'
    author.affiliation=u'University of kolingemstuff'
    author.save()

    coauthor = Author(
      fullname=u'Jenna Rapunzel',
      affiliation=u'Open University of Maliningrad'
    )
    coauthor.save()
    
    self.story = Story(
        title=u'The happy story of the Promo', 
        abstract=u'Considering the changes in the new brand buzz, the happy story has an happy ending',
        contents=u'## Basic \n\nWith a nice paragraph[^1] and some footnotes.\n\n### this is a third level\n\nsome text...\n\n[^1]: footnote content',
        owner=self.user
    )
    self.story.save()
    self.story.authors.add(coauthor)
    self.assertTrue(os.path.exists(self.story.get_path()))


  def _test_postgres_full_search(self):
    search_vector_contents = self.story.update_search_vector()
    self.assertEquals(len(search_vector_contents), 2)
    self.assertEquals(search_vector_contents[1][0], u'Basic\n\n\nWith a nice paragraph\n1\n and some footnotes.\n\n\nthis is a third level\n\n\nsome text...\n\n\n\n\n\n\n\n\n\n\nfootnote content&#160;\n&#8617;\n\n\n\n\n\n')


  #def _test_git_tag(self):



  def test_comment(self):
    # add comment
    com = Comment(story=self.story, contents=u'{}', owner=self.user)
    com.save()
    self.assertEquals(com.highlights, '')
    # print com.short_url



  def _test_download_docx(self):
    path = self.story.download(outputFormat='docx')
    self.assertTrue(os.path.exists(path))


  def _test_download_pdf(self):
    path = self.story.download(outputFormat='pdf')
    self.assertTrue(os.path.exists(path))

  def _test_delete(self):
    path = self.story.get_path()
    self.story.delete()
    self.assertFalse(os.path.exists(path))

    
  def _test_delete_user(self):
    path = self.user.profile.get_path()
    self.user.delete()
    self.assertFalse(os.path.exists(path))
   
    
  def test_suite(self):
    self._test_postgres_full_search()
    self._test_download_pdf()
    self._test_delete()
    self._test_delete_user()




class StoryCaptionTest(TestCase):
  """
  # python manage.py test miller.test.test_models_story.StoryCaptionTest
  """
  def setUp(self):
    self.user = User.objects.create_user(
        username='test-user-profile', 
        email='jacob@jacob', 
        password='top_secret')

    self.story, created = Story.objects.get_or_create(
        title=u'The happy story of the Promo', 
        abstract=u'Considering the changes in the new brand buzz, the happy story has an happy ending',
        contents=u'## Basic \n\nWith a nice paragraph[^1] and some footnotes.\n\n### this is a third level\n\nsome text...\n\n[^1]: footnote content',
        owner=self.user
    )

    # bulk create do not sending pre_save or post_save signal, the slug must be created manually
    self.documents = Document.objects.bulk_create([Document(
      title=u'Document %s' % k, 
      slug=u'document-%s' % k,
      owner=self.user,
      data={
        'title': u'Document %s' % k, 
        'description': u'This is the document %s' %k
      },
    ) for k in ['a', 'b', 'c', 'd']])


  def test_save_captions_from_contents(self):
    self.assertEquals(len(self.documents), 4)

    self.story.contents = json.dumps({
      'modules': [
        {
          'document': {
            'slug': 'document-a',
            'related':[
              {
                'slug': 'document-b',
              }
            ]
          }
        }
      ], 
      'overlay': {
        'background': {
          'slug': 'document-d'
        }
      }
    }, ensure_ascii=False)

    saved, missing, expected = self.story.save_captions_from_contents(key='slug')

    # chck that everything works as expected
    self.assertEquals(len(saved), 3)
    self.assertEquals(self.story.documents.count(), 3)
    self.assertEquals(expected, ['document-a', 'document-b', 'document-d'])
    self.assertFalse(missing)

    # now with non existing stuffs...
    self.story.contents = json.dumps({
      'modules': [
        {
          'document': {
            'slug': 'document-NOT-EXISTING',
            'related':[
              {
                'slug': 'document-b',
              }
            ]
          }
        }
      ], 
      'overlay': {
        'background': {
          'slug': 'document-d'
        }
      }
    }, ensure_ascii=False)

    saved, missing, expected = self.story.save_captions_from_contents(key='slug')

    self.assertEquals(len(saved), 2)
    self.assertEquals(self.story.documents.count(), 2)
    self.assertEquals(u'document-b,document-d', u','.join(self.story.documents.order_by('slug').values_list('slug', flat=True)))
    self.assertEquals(missing, [u'document-NOT-EXISTING'])







