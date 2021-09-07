prompts = [
    {
        'title': 'Add a "What we are reading" section to News Post page (back-end)',
        'description': '''
            In order to boost our editorial reputation, as a Dive Site Editor,
            I want to be able to add links to relevant sources which would appear at the end of newsposts.
            Editors should be able to add up to 3 "What we are reading" (WWAR) links per News Post. Some
            WWAR links will likely be used by more than one News Post, but they should be only available to
            the dive site on which they were created. Duplicate WWAR links on a given dive site should be prevented.
        ''',
        'AC': [
            'A new model and subsequent migration exist in the news app which will store WWAR links',
            'Model properties match the fields described in the scenarios',
            'Admin form matches the interactions described in the scenarios',
            'Limit News Posts to 3 WWAR links',
            'Any given WWAR link should be able to be associated with any News Post for the dive site it is on',
            'Users should not be able to save the same link twice on a dive site'
        ],
        'objectives': [
            'Understand how to create new models in Django',
            'Understand how to manage multiple models from one admin page in Django',
            'Understand many-to-many relationships in the Django ORM',
            'Understand how to create composite unique keys in Django',
            'Understand how SiteModel effects admin page interactions',
            'Understand how to customize an admin form save method to catch database constraint errors'
        ],
        'scenarios': [
            {
                'title': 'A WWAR model and admin pages exist under the news app',
                'steps': [
                    'Given I am a Dive Site Editor and I am signed in to the divesite admin',
                    'When I am on the admin home page',
                    'Then a link to "What We Are Reading" is listed under "NEWS"',
                ],
                'images': [
                    ('wwar/wwar-admin-home.png', 'Admin home page with WWAR section under News App')
                ]
            },
            {
                'title': 'An admin user can access a standard django admin Create form for WWAR links',
                'steps': [
                    'Given I am a Dive Site Editor and I on the "What We Are Reading" admin list page',
                    'When I click "ADD WHAT WE ARE READING +"',
                    'Then I see a form with the fields:',
                    '''
                    <table>
                        <tr><th>label</th><th>input type</th><th>help text</th></tr>
                        <tr><td>"title"</td><td>Text</td><td></td></tr>
                        <tr><td>"source"</td><td>URL</td><td></td></tr>
                        <tr>
                            <td>"published"</td>
                            <td>Date</td>
                            <td>"the date that the linked article was originally published"</td>
                        </tr>
                    </table>
                    '''
                ],
                'images': [
                    ('wwar/wwar-new.png', 'Example admin create page')
                ]
            },
            {
                'title': 'An admin user can add a WWAR link using standard admin pages',
                'steps': [
                    'Given I am a Dive Site Editor and I on the "What We Are Reading" create page',
                    'When I fill in the form with:',
                    '''
                    <table>
                        <tr><th>title</th><td>Macarena turns 25</td></tr>
                        <tr><th>link</th><td>https://www.theonion.com/macarena-turns-25-1847417240</td></tr>
                        <tr><th>source</th><td>The Onion</td></tr>
                        <tr><th>published</th><td>08/03/2021</td></tr>
                    </table>
                    ''',
                    'And I press "save"',
                    'Then I see a success message'
                ],
                'images': [
                    ('wwar/wwar-save-success.png', 'Successful WWAR save')
                ]
            },
            {
                'title': 'An admin user <strong>can not</strong> add the same WWAR link twice on a <strong>single dive site</strong>',  # noqa
                'steps': [
                    'Given I am a Dive Site Editor for YYY Dive',
                    'And I on the "What We Are Reading" create page',
                    'And the WWAR links exist:',
                    '''
                    <table>
                        <tr><th>site</th><th>link</th></tr>
                        <td>YYY</td>
                        <td>https://www.theonion.com/macarena-turns-25-1847417240</td>
                        </tr>
                        <tr>
                        <td>ZZZ</td>
                        <td>https://www.theonion.com/elizabeth-holmes-arrives-to-trial-with-prototype-for-bl-1847584107</td>
                        </tr>
                    </table>
                    ''',
                    'When I fill in the form with:',
                    '''
                    <table>
                        <tr><th>title</th><td>Macarena turns 25</td></tr>
                        <tr><th>link</th><td>https://www.theonion.com/macarena-turns-25-1847417240</td></tr>
                        <tr><th>source</th><td>The Onion</td></tr>
                        <tr><th>published</th><td>08/03/2021</td></tr>
                    </table>
                    ''',
                    'And I press save',
                    'Then I see a form vaidation error message',
                ],
                'images': [
                    ('wwar/wwar-form-error.png', 'Custom validation error on create page'),
                    ('wwar/wwar-uncaught-error.png',
                        'Replace this uncaught validation error page, which is the default behavior'),
                ]
            },
            {
                'title': 'An admin user <strong>can</strong> add the same WWAR link twice on a <strong>different dive sites</strong>',  # noqa
                'steps': [
                    'Given I am a Dive Site Editor for ZZZ Dive',
                    'And I on the "What We Are Reading" create page',
                    'And the WWAR links exist:',
                    '''
                    <table>
                        <tr><th>site</th><th>link</th></tr>
                        <td>YYY</td>
                        <td>https://www.theonion.com/macarena-turns-25-1847417240</td>
                        </tr>
                        <tr>
                        <td>ZZZ</td>
                        <td>https://www.theonion.com/elizabeth-holmes-arrives-to-trial-with-prototype-for-bl-1847584107</td>
                        </tr>
                    </table>
                    ''',
                    'When I fill in the form with:',
                    '''
                    <table>
                        <tr><td>title</td><td>Macarena turns 25</td></tr>
                        <tr><td>link</td><td>https://www.theonion.com/macarena-turns-25-1847417240</td></tr>
                        <tr><td>source</td><td>The Onion</td></tr>
                        <tr><td>published</td><td>08/03/2021</td></tr>
                    </table>
                    ''',
                    'And I press save',
                    'Then I see a success message',
                ]
            },
            {
                'title': 'Admin user can add up to 3 WWAR Links to a News Post from the News Post detail form page',
                'steps': [
                    'Given I am a Dive Site Editor and I am signed in to the divesite admin',
                    'When I go to a newspost detail edit page',
                    'And I scroll to the bottom of the form',
                    'Then I see a "What we are reading" inline form',
                    'And I can select existing WWAR links to add to this News Post',
                    'And I can remove WWAR links from this News Post',
                ],
                'images': [
                    ('wwar/wwar-inline-1.png',
                        'Example stacked inline form, which can associate WWAR Links to NewsPosts'),
                ]
            },
            {
                'title': 'Admin user <strong>cannot add more than 3</strong> WWAR Links to a News Post from the News Post detail form page',  # noqa
                'steps': [
                    'Given I am a Dive Site Editor and I am on a News Post detail admin page',
                    'When I add 3 WWAR Links to the News Post',
                    'Then the "Add another" button is hidden'
                ],
                'images': [
                    ('wwar/wwar-inline-maxed.png',
                        'Note that the "add another..." button no longer shows when the max of 3 instances has been reached')  # noqa
                ]
            }
        ]
    },
    {
        'title': 'Add a "What we are reading" section to News Post page (front-end)',
        'description': '''
            In order to get more information about topics covered on a given Dive Site story, as a reader,
            I want a list with links to related coverage from other sources.
        ''',
        'AC': [
            'A new feed section is added to the newspost template which contains the WWAR links associated with a given News Post',  # noqa
            'The title of the section should be "What we\'re reading"',
            'The sub-title of the section should be "Sources from other publications"',
            'The title of each feed item should be the title of the WWAR link and link to the URL',
            'Links should open in a new tab',
            'The secondary label for each item should be "<source name> • <pub month> <pub day>, <pub year>',
            'The layout should match the attached screenshot mockups',
            'The new content should be in the "pre footer" section of the page'
        ],
        'objectives': [
            'Understand how to create a feed using Snorkel',
            'Understand how to use blocks in Django templates',
            'Understand how use conditionals in Django templates',
        ],
        'scenarios': [
            {
                'title': 'A reader sees WWAR links in a section for the news post they are currently viewing',
                'steps': [
                    'Given I am a Dive Site Reader',
                    'And the WWAR links exist:',
                    '''
                        <table>
                        <tr><th>News Post ID</th><th>WWAR Link</th></tr>
                        <tr>
                        <td>ZZZ</td>
                        <td>"Click On Some Ads Around This Article And We’ll Split The Loot 60/40"</td>
                        </tr>
                        <tr>
                        <td>ZZZ</td>
                        <td>"Man Who Comfortably Achieved Yoga Pose Doing It Completely Wrong"</td>
                        </tr>
                        <tr>
                        <td>ZZZ</td>
                        <td>"Nation\'s Stage Managers Announce 5 Minutes To Places"</td>
                        </tr>
                        <tr>
                        <td>YYY</td>
                        <td>"Macarena turns 25"</td>
                        </tr>
                        <tr>
                        <td>YYY</td>
                        <td>"Elizabeth Holmes Arrives To Trial With Prototype For Black Box
                        That Will Prove Her Innocence"</td>
                        </tr>
                        <tr>
                        <td>YYY</td>
                        <td>"Man Arrested For Stealing 21 Tons Of Pistachios"</td>
                        </tr>
                        </table>
                    ''',
                    'When I am on the News Post ZZZ detail page',
                    'Then the newspost contains a "What we are reading" section',
                    'And the "What we are reading" section contains the links',
                    '''
                        <table>
                        <tr><th>WWAR Link</th></tr>
                        <tr>
                        <td>"Click On Some Ads Around This Article And We’ll Split The Loot 60/40"</td>
                        </tr>
                        <tr>
                        <td>"Man Who Comfortably Achieved Yoga Pose Doing It Completely Wrong"</td>
                        </tr>
                        <tr>
                        <td>"Nation\'s Stage Managers Announce 5 Minutes To Places"</td>
                        </tr>
                        </table>
                    ''',
                ],
                'images': [
                    ('wwar/wwar-mockup.png',
                        'Example mockup'),
                    ('wwar/wwar-mockup-close.png',
                        'Close up')
                ],
            },
            {
                'title': 'WWAR section is hidden when there are no WWAR links for a given News Post',
                'steps': [
                    'Given I am a Dive Site Reader',
                    'And there are no WWAR links saved for News Post ZZZ',
                    'When I am on the News Post ZZZ detail page',
                    'Then the WWAR section is hidden'
                ],
                'images': [
                    ('wwar/wwar-nolinks.png', ''),
                ],
            },
        ]
    },
    {
        'title': 'Add Related Dives functionality to admin',
        'AC': [
            'A new model exists in the Taxonomy app which allows admin users to associate Dive Sites to eachother',
            'A given Dive Site cannot be added to the same site more than once'
        ],
        'objectives': [
            'Understand how to create new models in Django',
            'Understand many-to-many relationships in the Django ORM',
            'Understand how to create composite unique keys in Django',
            'Understand how SiteModel effects admin page interactions',
            'Understand how to customize an admin form save method to catch database constraint errors',
        ],
        'description': '''
            In order to begin associating editorial content across different Dive Sites,
            as a Dive Site Editor, I want to be able to link Dives that are closely related
            to eachother (e.g., Restaraunt Dive and Retail Dive may be closely related to Supply Chain Dive).
        ''',
        'scenarios': [
            {
                'title': 'Related Dives can be accessed from the Admin page',
                'steps': [
                    'Given I am a Dive Site Editor',
                    'And I am logged in to the Admin',
                    'Then a link to "Related Dives" is under the "Taxonomy" header'
                ],
            },
            {
                'title': 'Editor can add a Related Dive',
                'steps': [
                    'Given I am a Dive Site Editor',
                    'And I am logged in to the Retail Dive Admin',
                    'And I am on the add Related Dives page',
                    'When I select "Supply Chain Dive" for "Related Dive"',
                    'And I press "save"',
                    'Then I see a confirmation message'
                ],
            },
            {
                'title': 'Editor can not add the same Related Dive more than once',
                'steps': [
                    'Given I am a Dive Site Editor',
                    'And a Related Dive instance for "Supply Chain Dive" exists',
                    'And I am logged in to the Retail Dive Admin',
                    'And I am on the add Related Dives page',
                    'When I select "Supply Chain Dive" for "Related Dive"',
                    'And I press "save"',
                    'Then I see an error message',
                    'And the Create page is re-loaded'
                ],
            }
        ]
    },
    {
        'title': 'Set up related Dive Sites for Editorial Team',
        'AC': [
            'A custom migration is created that links the following divesites to eachother:',
            '''
            <table>
                <tr>
                    <th>Site</th>
                    <th>Related sites</th>
                </tr>
                <tr>
                    <td>Retail Dive</td>
                    <td>
                        Supply Chain Dive<br />
                        Grocery Dive
                    </td>
                </tr>
                <tr>
                    <td>Restaraunt Dive</td>
                    <td>
                        Supply Chain Dive<br />
                        Grocery Dive<br />
                    </td>
                </tr>
                <tr>
                    <td>Grocery Dive</td>
                    <td>
                        Supply Chain Dive<br />
                        Restaraunt Dive<br />
                    </td>
                </tr>
                <tr>
                    <td>Supply Chain Dive</td>
                    <td>
                        Retail Dive<br />
                        Grocery Dive<br />
                        Restaraunt Dive
                    </td>
                </tr>
            </table>
            ''',
            'This migration can be run forward and backward. If reversed, it should remove all Related Dive instances'
        ],
        'objectives': [
            'Understand how to create custom migrations in Django that are backward and forward compatible',
        ],
        'description': '''
            In order to make sure that the correct related dive sites are linked together, as a Dive Site Editor, I
            want the engineering team to pre-populate the existing related Dive Sites.
        ''',
    },
    {
        'title': 'Add a "Related Coverage" sidebar box',
        'AC': [
            'Any page that includes a sidebar should have a "Related Coverage" box',
            'The related coverage box should contain 5 News Posts from related Dive Sites in a random order',
            'The first related post should include its image',
            'The related posts should be set via a context processor so that they are available to any page',
            'If there are no Related Dive Sites OR fewer than 5 News Posts across related Dive Sites, the "Related Coverage" box should be hidden',  # noqa
            'The "Related Coverage" box should match the mocks and use HTML and CSS found in Snorkel',
            'The "Related Coverage" box should appear below the signup sidebar box',

        ],
        'objectives': [
            'Understand how to access Site object data across Sites',
            'Understand how to work with custom context processors',
            'Understand how to build a sidebar box using Snorkel'
        ],
        'description': '''
            In order to get information related content I am reading on a given Dive Site, as
            a Dive Site Reader, I want to see news posts from other Dive Sites that are related
            to the one I am currently on.
        ''',
        'scenarios': [
            {
                'title': 'Display news posts from related Dive Sites in sidebar when there are at least 5 available related News Posts',  # noqa
                'steps': [
                    'Given I am a Retail Dive Reader',
                    'And 5 News Posts exist on related Dives',
                    'When I am on the Front Page',
                    'Then the "Related Coverage" is visible',
                    'And the "Related Coverage" contains 4 stories',
                ],
                'images': []
            },
            {
                'title': 'Hide "Related Coverage" sidebar box when there are no related Dive Sites',
                'steps': [
                    'Given I am a Retail Dive Reader',
                    'And Retail Dive has no related Dives',
                    'When I am on the Front Page',
                    'Then the "Related Coverage" is hidden',
                ],
                'images': []
            },
            {
                'title': 'Hide "Related Coverage" sidebar box when there are less than 5 related Dive Site News Posts',
                'steps': [
                    'Given I am a Retail Dive Reader',
                    'And 4 News Posts exist on related Dives',
                    'When I am on the Front Page',
                    'Then the "Related Coverage" is hidden',
                ],
                'images': [
                    ('related-posts/related-posts-placement-archive.png',
                        'Example mockup in correct placement on archive page'),
                    ('related-posts/related-posts-placement-story.png',
                        'Example mockup in correct placement on news post page'),
                    ('related-posts/related-posts-full.png',
                        'Full mockup of box')
                ],
            }
        ]
    },
    # {
    #     'title': 'Add a search form to archive page',
    #     'AC': [],
    #     'objectives': [],
    #     'description': '''
    #     ''',
    #     'scenarios': [
    #         {
    #             'title': '',
    #             'steps': [],
    #             'images': []
    #         }
    #     ]
    # },
]

"""
    'title': '',
    'AC': [],
    'objectives': [],
    'description': '''
    ''',
    'scenarios': [
        {
            'title': '',
            'steps': [],
            'images': []
        }
    ]
"""
