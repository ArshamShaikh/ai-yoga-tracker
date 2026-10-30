import React, { useState, useMemo } from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity, Dimensions, TextInput, Image } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { useRouter } from 'expo-router';
import { FontAwesome5 } from '@expo/vector-icons';
import poseData from '../../src/constants/poseConstraints.json';
import { getPoseMetadata } from '../../src/constants/poseVisuals';
import { getPoseImage } from '../../src/constants/poseImages';
import PoseGuideModal from '../../src/components/PoseGuideModal';

const { width } = Dimensions.get('window');
const COLUMN_COUNT = 2;
const PADDING = 16;
const CARD_WIDTH = (width - (PADDING * 2) - 12) / COLUMN_COUNT;

export default function PosesLibrary() {
    const router = useRouter();
    const [selectedCategory, setSelectedCategory] = useState('all');
    const [searchQuery, setSearchQuery] = useState('');
    const [selectedGuidePose, setSelectedGuidePose] = useState(null);
    const [guideVisible, setGuideVisible] = useState(false);

    const handleOpenGuide = (pose) => {
        setSelectedGuidePose(pose);
        setGuideVisible(true);
    };

    const handleStartSession = (poseId) => {
        setGuideVisible(false);
        router.push({ pathname: '/session', params: { targetPose: poseId } });
    };

    const getDifficultyColor = (diff) => {
        switch (diff) {
            case 'advanced': return { bg: '#FEE2E2', text: '#991B1B' };
            case 'intermediate': return { bg: '#FEF3C7', text: '#92400E' };
            case 'beginner':
            default:
                return { bg: '#E8F5E9', text: '#1B4D3E' };
        }
    };

    const filteredPoses = useMemo(() => {
        return poseData.yoga_poses.filter(pose => {
            const matchesCategory = selectedCategory === 'all' || pose.orientation === selectedCategory;
            const q = searchQuery.toLowerCase().trim();
            const matchesSearch = !q ||
                pose.name.toLowerCase().includes(q) ||
                (pose.sanskrit && pose.sanskrit.toLowerCase().includes(q));
            return matchesCategory && matchesSearch;
        });
    }, [selectedCategory, searchQuery]);

    return (
        <SafeAreaView style={styles.safeArea} edges={['top', 'left', 'right']}>
            <View style={styles.container}>
                {/* Studio Header */}
                <View style={styles.headerArea}>
                    <Text style={styles.headerSubtitle}>ASANA REPOSITORY</Text>
                    <Text style={styles.header}>Yoga Pose Library</Text>
                    <Text style={styles.subHeader}>{poseData.yoga_poses.length} Poses Available • 3D Biomechanics</Text>
                </View>

                {/* Search Input Bar */}
                <View style={styles.searchWrapper}>
                    <View style={styles.searchBar}>
                        <FontAwesome5 name="search" size={14} color="#9CA3AF" style={{ marginRight: 10 }} />
                        <TextInput
                            style={styles.searchInput}
                            placeholder="Search pose (e.g. Warrior, Down Dog, Vrikshasana)..."
                            placeholderTextColor="#9CA3AF"
                            value={searchQuery}
                            onChangeText={setSearchQuery}
                            clearButtonMode="while-editing"
                        />
                        {searchQuery.length > 0 && (
                            <TouchableOpacity onPress={() => setSearchQuery('')}>
                                <FontAwesome5 name="times-circle" size={14} color="#9CA3AF" />
                            </TouchableOpacity>
                        )}
                    </View>
                </View>

                {/* Category Filter Strip */}
                <View style={styles.filterWrapper}>
                    <ScrollView
                        horizontal
                        showsHorizontalScrollIndicator={false}
                        contentContainerStyle={styles.filterContent}
                    >
                        <TouchableOpacity
                            style={[styles.filterPill, selectedCategory === 'all' && styles.filterPillActive]}
                            onPress={() => setSelectedCategory('all')}
                            activeOpacity={0.8}
                        >
                            <Text style={[styles.filterText, selectedCategory === 'all' && styles.filterTextActive]}>
                                All ({poseData.yoga_poses.length})
                            </Text>
                        </TouchableOpacity>
                        {poseData.categories.map((category) => {
                            const count = poseData.yoga_poses.filter(p => p.orientation === category.id).length;
                            return (
                                <TouchableOpacity
                                    key={category.id}
                                    style={[styles.filterPill, selectedCategory === category.id && styles.filterPillActive]}
                                    onPress={() => setSelectedCategory(category.id)}
                                    activeOpacity={0.8}
                                >
                                    <Text style={[styles.filterText, selectedCategory === category.id && styles.filterTextActive]}>
                                        {category.label} {count > 0 ? `(${count})` : ''}
                                    </Text>
                                </TouchableOpacity>
                            );
                        })}
                    </ScrollView>
                </View>

                {/* 2-Column Responsive Pose Cards */}
                <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
                    {filteredPoses.length === 0 ? (
                        <View style={styles.emptyStateBox}>
                            <FontAwesome5 name="search" size={32} color="#D1D5DB" />
                            <Text style={styles.emptyStateTitle}>No Poses Found</Text>
                            <Text style={styles.emptyStateSub}>Try clearing your search query or choosing another filter.</Text>
                        </View>
                    ) : (
                        <View style={styles.grid}>
                            {filteredPoses.map((pose) => {
                                const diffStyle = getDifficultyColor(pose.difficulty);
                                const meta = getPoseMetadata(pose.id);
                                const iconName = meta?.icon || 'spa';
                                const accentColor = meta?.accentColor || '#1B4D3E';
                                const poseImg = getPoseImage(pose.id);

                                return (
                                    <TouchableOpacity
                                        key={pose.id}
                                        style={styles.card}
                                        onPress={() => handleOpenGuide(pose)}
                                        activeOpacity={0.85}
                                    >
                                        <View style={styles.cardTopRow}>
                                            <View style={[styles.diffBadge, { backgroundColor: diffStyle.bg }]}>
                                                <Text style={[styles.diffText, { color: diffStyle.text }]}>
                                                    {pose.difficulty ? pose.difficulty.toUpperCase() : 'BEGINNER'}
                                                </Text>
                                            </View>
                                            <Text style={styles.jointCountText}>
                                                {pose.joints?.length || 2} Pts
                                            </Text>
                                        </View>

                                        <View style={styles.cardImageBox}>
                                            {poseImg ? (
                                                <Image
                                                    source={poseImg}
                                                    style={styles.cardPoseImage}
                                                    resizeMode="contain"
                                                />
                                            ) : (
                                                <View style={[styles.iconFallbackCircle, { backgroundColor: `${accentColor}1A` }]}>
                                                    <FontAwesome5 name={iconName} size={28} color={accentColor} />
                                                </View>
                                            )}
                                        </View>

                                        <View style={styles.cardBody}>
                                            <Text style={styles.cardTitle} numberOfLines={1}>{pose.name}</Text>
                                            <Text style={styles.sanskritSubtitle} numberOfLines={1}>{pose.sanskrit || pose.name}</Text>
                                        </View>
                                    </TouchableOpacity>
                                );
                            })}
                        </View>
                    )}
                </ScrollView>
            </View>

            {/* Educational Pose Guide Modal */}
            <PoseGuideModal
                visible={guideVisible}
                pose={selectedGuidePose}
                onClose={() => setGuideVisible(false)}
                onStartSession={handleStartSession}
            />
        </SafeAreaView>
    );
}

const styles = StyleSheet.create({
    safeArea: {
        flex: 1,
        backgroundColor: '#F7F8F9',
    },
    container: {
        flex: 1,
        backgroundColor: '#F7F8F9',
    },
    headerArea: {
        paddingHorizontal: PADDING,
        paddingTop: 12,
        paddingBottom: 6,
    },
    headerSubtitle: {
        fontSize: 10,
        fontWeight: '800',
        color: '#1B4D3E',
        letterSpacing: 1.2,
        marginBottom: 2,
    },
    header: {
        color: '#111827',
        fontSize: 26,
        fontWeight: '800',
        letterSpacing: -0.5,
    },
    subHeader: {
        color: '#6B7280',
        fontSize: 13,
        fontWeight: '500',
        marginTop: 2,
    },
    searchWrapper: {
        paddingHorizontal: PADDING,
        paddingTop: 8,
        paddingBottom: 6,
    },
    searchBar: {
        flexDirection: 'row',
        alignItems: 'center',
        backgroundColor: '#FFFFFF',
        borderRadius: 14,
        paddingHorizontal: 14,
        paddingVertical: 10,
        borderWidth: 1,
        borderColor: '#E5E7EB',
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 1 },
        shadowOpacity: 0.03,
        shadowRadius: 3,
        elevation: 1,
    },
    searchInput: {
        flex: 1,
        fontSize: 14,
        color: '#111827',
        padding: 0,
    },
    filterWrapper: {
        paddingVertical: 8,
    },
    filterContent: {
        paddingHorizontal: PADDING,
        gap: 8,
    },
    filterPill: {
        paddingHorizontal: 14,
        paddingVertical: 7,
        borderRadius: 20,
        backgroundColor: '#FFFFFF',
        borderWidth: 1,
        borderColor: '#E5E7EB',
        justifyContent: 'center',
        alignItems: 'center',
    },
    filterPillActive: {
        backgroundColor: '#1B4D3E',
        borderColor: '#1B4D3E',
    },
    filterText: {
        color: '#4B5563',
        fontSize: 12,
        fontWeight: '600',
    },
    filterTextActive: {
        color: '#FFFFFF',
    },
    scrollContent: {
        paddingHorizontal: PADDING,
        paddingBottom: 40,
        paddingTop: 4,
    },
    grid: {
        flexDirection: 'row',
        flexWrap: 'wrap',
        justifyContent: 'space-between',
        rowGap: 12,
    },
    card: {
        width: CARD_WIDTH,
        backgroundColor: '#FFFFFF',
        padding: 12,
        borderRadius: 18,
        borderWidth: 1,
        borderColor: '#E5E7EB',
        shadowColor: '#000',
        shadowOffset: { width: 0, height: 2 },
        shadowOpacity: 0.04,
        shadowRadius: 6,
        elevation: 2,
        justifyContent: 'space-between',
        minHeight: 185,
    },
    cardTopRow: {
        flexDirection: 'row',
        justifyContent: 'space-between',
        alignItems: 'center',
        marginBottom: 6,
    },
    cardImageBox: {
        height: 95,
        width: '100%',
        alignItems: 'center',
        justifyContent: 'center',
        backgroundColor: '#F9FAFB',
        borderRadius: 12,
        marginVertical: 4,
        padding: 6,
    },
    cardPoseImage: {
        width: '100%',
        height: '100%',
    },
    iconFallbackCircle: {
        width: 50,
        height: 50,
        borderRadius: 25,
        alignItems: 'center',
        justifyContent: 'center',
    },
    diffBadge: {
        paddingHorizontal: 7,
        paddingVertical: 3,
        borderRadius: 8,
    },
    diffText: {
        fontSize: 9,
        fontWeight: '800',
        letterSpacing: 0.5,
    },
    cardBody: {
        justifyContent: 'center',
        paddingTop: 6,
    },
    cardTitle: {
        color: '#111827',
        fontSize: 14,
        fontWeight: '700',
        marginBottom: 1,
    },
    sanskritSubtitle: {
        color: '#6B7280',
        fontSize: 11,
        fontStyle: 'italic',
        fontWeight: '500',
    },
    cardFooter: {
        flexDirection: 'row',
        justifyContent: 'space-between',
        alignItems: 'center',
        marginTop: 8,
        paddingTop: 8,
        borderTopWidth: 1,
        borderTopColor: '#F3F4F6',
    },
    jointCountText: {
        color: '#9CA3AF',
        fontSize: 11,
        fontWeight: '600',
    },
    infoIconBox: {
        width: 20,
        height: 20,
        borderRadius: 10,
        justifyContent: 'center',
        alignItems: 'center',
    },
    emptyStateBox: {
        alignItems: 'center',
        justifyContent: 'center',
        paddingVertical: 60,
    },
    emptyStateTitle: {
        fontSize: 16,
        fontWeight: '700',
        color: '#374151',
        marginTop: 12,
    },
    emptyStateSub: {
        fontSize: 13,
        color: '#9CA3AF',
        marginTop: 4,
        textAlign: 'center',
        paddingHorizontal: 20,
    },
});
