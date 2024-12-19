from django.views.generic import TemplateView
from content.models import MoviePoster, ConcessionItem, TicketPrice
from collections import defaultdict


class HomeView(TemplateView):
    template_name = 'coreWebsite/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch the latest movie poster
        context['movie_poster'] = MoviePoster.objects.last()

        # Add showtimes and promotions
        context['showtimes'] = {
            'title': 'Mufasa',
            'dates': '12/19 - 12/22',
            'times': [
                {'day': 'Thurs', 'time': '6pm'},
                {'day': 'Fri', 'time': '6pm'},
                {'day': 'Sat', 'time': '2pm / 6pm'},
                {'day': 'Sun', 'time': '2pm / 6pm'},
            ],
        }
        context['promotion'] = 'GIVEAWAY'

        return context


class AboutView(TemplateView):
    template_name = 'coreWebsite/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['faqs'] = [
            {"question": "Are most of your shows sold out?", "answer": "You may see a line of people outside our door, but the Loma has only ever had 3 sellouts in the four years of being open. You can purchase tickets in advance at our box office or online at https://www.atomtickets.com/theaters/the-loma-theater/12346."},
            {"question": "Do NMT students get into shows for free?", "answer": "The Loma Theater does not grant free admission to Tech students, but we offer a student discount. Many free student shows are sponsored by student groups throughout the school year. Contact NMT Student Government Association for details."},
            {"question": "Why don't you show more than one movie at a time, and why do you keep the same movie for two weeks or longer?", "answer": "We book our movies through the movie studios. They set the terms for what we can show and for how long."},
            {"question": "When did the theater reopen and who actually owns it?", "answer": "The theater was reopened November 1, 2017. First State Bank owns the theater, NMT remodeled and provided equipment, and the business is owned by On the Break Entertainments, LLC."},
            {"question": "Why are you only open on the weekends?", "answer": "We are considered a 'weekend theatre' by the movie industry. As Socorro grows, the needs for a 'calendar theater' will be considered."},
            {"question": "How many seats are in the theater?", "answer": "217"},
            {"question": "Can I rent out the theater for a private showing? Do you offer field trips for schools?", "answer": "Email lomatheater.com for rental details. Schools receive special discounts for field trips."},
            {"question": "Why do some movies have black bars on each side of the picture?", "answer": "Movies are filmed in either scope or flat format. Flat format movies have bars on each side."},
            {"question": "Why are free movie passes considered 'free' but cost $8.00 to purchase?", "answer": "Movie passes are typically bought as gifts or prizes, allowing recipients to see any movie for free."},
            {"question": "Do I have to stay and watch the movie with my child, or can I drop them off?", "answer": "The Loma is not responsible for unattended children. Policies vary based on the time of the show, with specific rules for children under 16. Parents are encouraged to attend and create happy memories."},
            {"question": "Are you hiring?", "answer": "We are always accepting applications due to our dynamic staff. Please apply using our form."},
        ]
        return context


class ConcessionsView(TemplateView):
    template_name = 'coreWebsite/concessions.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        concessions = ConcessionItem.objects.all().order_by('category', 'name')
        grouped_concessions = defaultdict(list)
        for item in concessions:
            grouped_concessions[item.category].append(item)
        context['grouped_concessions'] = grouped_concessions
        return context


class TicketPricesView(TemplateView):
    template_name = 'coreWebsite/ticket_prices.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Group ticket prices by category and then by showtime
        grouped_ticket_prices = defaultdict(lambda: defaultdict(list))
        for ticket in TicketPrice.objects.all().order_by('category', 'showtime', 'age_group'):
            grouped_ticket_prices[ticket.category][ticket.showtime].append(ticket)

        context['grouped_ticket_prices'] = grouped_ticket_prices
        return context


class ContactView(TemplateView):
    template_name = 'coreWebsite/contact.html'
