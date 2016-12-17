#Author:  Justin Stevens
#Purpose:  Solves the missionaries and cannibals puzzle for any variables using a Breadth-first earch
#Date:  June 2015
class Queue:
    def __init__(self):
        self.array=[]
    def enqueue(self, thing):
        self.array.append(thing)
    def dequeue(self):
        store=self.array[0]
        del self.array[0]
        return store

class Stack:
    def __init__(self):
        self.array=[]
    def push(self, thing):
        self.array.append(thing)
    def pop(self):
        store=self.array[-1]
        del self.array[-1]
        return store
    def Empty(self):
        return len(self.array)==0
class Setup:
    def __init__(self, cannibal, missionarie, boat):
        self.cannibal=cannibal
        self.missionarie=missionarie
        self.boat=boat

def Generate_Neighbors(node, g):
    """Generates neighbors of the node"""
    #generate in the class
    x=node.state[0]
    y=node.state[1]
    z=node.state[2]
    output=[]
    #when the boat is on the left side
    if z==1:
        possible_moves=[]
        #maximum of g.boat people on the boat at a time
        for i in range(1, g.boat+1):
            for j in range(0, i+1):
                #make a list of all possible moves
                possible_moves.append([x-j, y-i+j, 0])
        for [a,b,c] in possible_moves:
            #conditions necessary for the cannibals to not outnumber the missionaries
            if g.cannibal>=a>=0 and g.missionarie>=b>=0 and (a<=b or b==0) and (g.missionarie-b>=g.cannibal-a or b==g.missionarie):
                output.append(Node([a,b,c], node))
            else:
                continue
        return output
    if z==0:
        #maximum of two people on the boat at a time
        possible_moves=[]
        for i in range(1, g.boat+1):
            for j in range(0, i+1):
                #make a list of all possible moves
                possible_moves.append([x+j, y+i-j, 1])
        for [a,b,c] in possible_moves:
            #conditions necessary for the cannibals to not outnumber the missionaries
            if g.cannibal>=a>=0 and g.missionarie>=b>=0 and (a<=b or b==0) and (g.missionarie-b>=g.cannibal-a or b==g.missionarie):
                output.append(Node([a,b,c], node))
            else:
                continue
        return output


def Search(g):
    """Returns all the visited nodes in the game"""
    #make a queue
    q=Queue()
    #define a starting node for the starting game state
    node=Node([g.cannibal,g.missionarie,1], None)
    #make the parent node itself; will be used in a while loop in main() to terminate the print function
    node.parent=node
    visited=[node]
    #queue up the starting node
    q.enqueue(node)
    #while the queue has elements in it
    while q.array:
        #dequeue the node as we have it saved now
        top = q.dequeue()
        #for each neighbor of the node
        for neighbor in Generate_Neighbors(top, g):
            if neighbor not in visited:
                #enqueue the node going back to top
                q.enqueue(neighbor)
                visited.append(neighbor)
    return visited

def FindParents(node):
    """For a given node, finds a parent node"""
    return node.parent

class Node:
    #creating a node class with two parameters:  state and parent
    #state will be used to determine the game state, which will consist of a list of three elements
    #parent will consist of a node determining the previous game state
    #once the search function finishes, the parent state will be used to determine the moves used to get to [0,0,0]
    def __init__(self, state, parent):
        self.state=state
        self.parent=parent
    #formating of the node
    def __str__(self):
        return "Node({0}, {1})".format(self.state, id(self.parent))
    #redefines equality as each time we make a new node, it will be different even if self.state is the same
    def __eq__(self, other):
        #print self, other
        return self.state==other.state
def instructions():
    print \
    """
***Instructions:***

Some missionaries and some cannibals attempt to cross a river with a boat.

There are two sides to the river.

The boat cannot cross the river by itself.

The cannibals cannot outnumber the missionaries on either side of the river, unless there are no missionaries.

The string <<<[??]>>> is used to represent which side of the river the boat is on (left or right).
    """



def ask_yes_no(question):
    """Ask a yes or no question"""
    response=None
    #if the user has not provided a sufficient answer, ask the question again
    while response not in ("y", "n"):
        response=raw_input(question).lower()
    return response

def rematch():
    #Used in the main() function with the answer to this stored in the variable yodawg
    answer=ask_yes_no("Do you want to try again? (y/n)")
    if answer=="y":
        print "\n \n"
        return True
    else:
        return False
def ask_number(question):
    answer=None

    while type(answer)!=type(0) and answer<0:
        try:
            answer=int(raw_input(question))
            answer=abs(answer)
        except:
            pass
    return answer



#main



def main():
    re=True
    while re:
        """Main function"""
        instructions()
        c=ask_number("How many cannibals will there be?")

        m=ask_number("How many missionaries will there be?")

        b=ask_number("How many people will be able to cross the boat at a time?")
        print "............................................................................................"
        print "\n"
        print "***This is a computer's solution to the problem using a search function:***"
        print "\n"
        g=Setup(c,m,b)
        s=Stack()
        #output is a result of all the nodes visited in the Search() function
        out=Search(g)
        #create an empty list which will be printed in the end
        list=[]
        begin=None
        for n in out:

            #finding the state [0,0,0] and it's corresponding id
            if n.state!=[0,0,0]:
                continue
            else:
                begin=n
                #push begin onto a stack
                s.push(begin)
        if not begin:
            print "Sorry, there are no solutions to the parameters you entered"
        while begin:
            new=FindParents(begin)
            s.push(new)
        #new.parents=new only when we are at the starting node of the search function
            while new.parent != new:
                new=FindParents(new)
                s.push(new)
            while not s.Empty():
                m=s.pop()
                list.append(m)
            counter=0
            for i in list:
                counter+=1
                print "Position", counter,":"
                cannibals=i.state[0]
                missionaries=i.state[1]
                boat=i.state[2]
                print "Left:  " ,cannibals, "cannibals and", missionaries ,"missionaries     Right: ", g.cannibal-cannibals, "cannibals and", g.missionarie-missionaries, "missionaries"
                if boat==0:
                    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<<<[??]>>> \n\n"
                elif boat==1:
                    print "<<<[??]>>>~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n\n"
            begin=None
        re=rematch()
main()
