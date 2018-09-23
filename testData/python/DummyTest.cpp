#include "db/Dummy.h"

namespace db
{

class DummyTest : public Test
{
public:
    int a;
};

TEST_F(DummyTest, haha)
{
    Dummy dummy;
    EXPECT_EQ(2,1);
}

}
