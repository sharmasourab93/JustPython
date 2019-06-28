
import webbrowser
from time import sleep


class Scheduler:
    """
    Aim of the program is to write an HTML file which receives
    an input from the python code in the form of a URL and then
    plays it in an enqueued manner
    """

    def __init__(self):
        self.in_queue = []
        
    def write_html(self, url):

        """Writes HTML to the File"""
        brk, indent, tabspace = '<br/>', "\n", "\t"

        a = open('test2.html', "w")
        a.truncate()
        a.write('<html>' + '\n' + '<body>')
        a.write(brk + indent)

        # Refresh the page
        a.write('<META HTTP-EQUIV="refresh" CONTENT="5"/>')
        a.write(brk + indent)
        a.write('<iframe width="560" height="315" src="' + url +
                '?autoplay=1" frameborder="0" allowfullscreen>')

        a.write(brk + indent)
        a.write('</iframe>')
        a.write(brk + indent + tabspace)

        a.write('Hello! ^ Your Video Plays Here ^')
        a.write(brk + indent)
        a.write('</body></html>')
        a.write(brk + indent)
        a.close()
        
    def push(self, obj):
        """To push objects into the queue"""

        self.in_queue.append(obj)

    def push_urls(self):
        """Dumb method Just to Push Urls into the Queue"""

        self.push('https://www.youtube.com/embed/9orjD9xj6z8')
        self.push('https://www.youtube.com/embed/OMJc43wUPLM')
        self.push('https://www.youtube.com/embed/ft-dYaZKxwU')
        self.push('https://www.youtube.com/embed/2fG9-W-OwCs')
        
    def action_block(self):
        """For taking actions"""
        location = r"<file-location>"
        self.push_urls()
        print(self.in_queue)
        i = 0

        while self.in_queue and i < len(self.in_queue):
            if i == 0:
                self.write_html(self.in_queue[i])
                # Open the Page
                webbrowser.open(location, new=0)

            else:
                self.write_html(self.in_queue[i])

            i = i + 1

            print('{} Video Playing'.format(i))

            sleep(5)

        print("All Videos Played for the day!")
        

if __name__ == '__main__':
    take_action = Scheduler()
    take_action.action_block()