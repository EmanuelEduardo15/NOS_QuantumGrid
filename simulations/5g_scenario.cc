#include "ns3/core-module.h"
using namespace ns3;

int main() {
    NodeContainer nodes;
    nodes.Create(1000);
    Config::SetDefault("ns3::NrAmc::ErrorModelType", StringValue("ns3::NrEesmCurvature"));
    Simulator::Run();
    return 0;
}
