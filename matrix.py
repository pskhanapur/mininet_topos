"""Custom topology example
Creates a matrix of switches with four host connected to each edge

e.g. 2x2 matrix
   host --- switch --- switch --- host
            |             |
   host --- switch --- switch --- host
   
e.g. 3x3 matrix
   host --- switch --- switch --- switch --- host
              |           |         |
            switch --- switch --- switch 
              |           |         |
   host --- switch --- switch --- switch  --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=matrix,2' from the command line.
Created by Prasanna Khanapur (pskhanapur@gmail.com). 
Feel free to contact creator for bug reporting, enhancements etc..
"""

from mininet.topo import Topo

class Matrix( Topo ):
    "Matrix topology example."

    def __init__( self , n ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )
        self.n = n


        # Add hosts and switches
        leftTopHost = self.addHost( 'h1' )
        rightTopHost = self.addHost( 'h2' )
        leftBottomHost = self.addHost( 'h3' )
        rightBottomHost = self.addHost( 'h4' )


        switches = []
        for i in range(1,n+1):
            for j in range(1,n+1):
                switches.append(self.addSwitch( 's' + str(j+((i-1)*n))))

        # Add links
        #self.addLink( leftHost, leftSwitch )

        for i in range(1,n+1):
            for j in range(1,n):
                firstswitch = 's'+ str(j+((i-1)*n))
                secondswitch = 's'+ str(j+((i-1)*n)+1)
                self.addLink(firstswitch,secondswitch)
        for i in range(1,n):
            for j in range(1,n+1):
                firstswitch = 's'+ str(j+((i-1)*n))
                secondswitch = 's'+ str(j+n+((i-1)*n))
                self.addLink(firstswitch,secondswitch)

        # Add links
        self.addLink( leftTopHost, 's1' )
        self.addLink( rightTopHost, 's'+ str(n))
        self.addLink( leftBottomHost, 's'+ str(n*n-n+1))
        self.addLink( rightBottomHost, 's' + str(n*n))


topos = { 'matrix': ( lambda n: Matrix(n) ) }

