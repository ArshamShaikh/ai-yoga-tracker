import { Tabs } from 'expo-router';
import { FontAwesome5 } from '@expo/vector-icons';

export default function TabLayout() {
    return (
        <Tabs
            screenOptions={{
                headerShown: false, // Let custom screen headers provide richer, tailored UX
                tabBarStyle: {
                    backgroundColor: '#FFFFFF',
                    borderTopColor: '#E5E7EB',
                    borderTopWidth: 1,
                    height: 64,
                    paddingBottom: 10,
                    paddingTop: 8,
                    elevation: 8,
                    shadowColor: '#000',
                    shadowOffset: { width: 0, height: -2 },
                    shadowOpacity: 0.04,
                    shadowRadius: 8,
                },
                tabBarActiveTintColor: '#1B4D3E',
                tabBarInactiveTintColor: '#9CA3AF',
                tabBarLabelStyle: {
                    fontSize: 11,
                    fontWeight: '700',
                    letterSpacing: 0.3,
                },
            }}>
            <Tabs.Screen
                name="index"
                options={{
                    title: 'Home',
                    tabBarLabel: 'Studio',
                    tabBarIcon: ({ color }) => <FontAwesome5 name="home" size={19} color={color} />,
                }}
            />
            <Tabs.Screen
                name="routines"
                options={{
                    title: 'Routines',
                    tabBarLabel: 'Flows',
                    tabBarIcon: ({ color }) => <FontAwesome5 name="fire" size={19} color={color} />,
                }}
            />
            <Tabs.Screen
                name="poses"
                options={{
                    title: 'Poses',
                    tabBarLabel: 'Library',
                    tabBarIcon: ({ color }) => <FontAwesome5 name="spa" size={19} color={color} />,
                }}
            />
            <Tabs.Screen
                name="activity"
                options={{
                    title: 'Activity',
                    tabBarLabel: 'Progress',
                    tabBarIcon: ({ color }) => <FontAwesome5 name="chart-line" size={19} color={color} />,
                }}
            />
        </Tabs>
    );
}
