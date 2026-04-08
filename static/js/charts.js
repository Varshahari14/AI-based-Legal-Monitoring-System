// AI Legal Monitoring System - Charts and Data Visualization

class LegalMonitorCharts {
    constructor() {
        this.charts = {};
        this.init();
    }

    init() {
        // Initialize charts when DOM is ready
        this.createComplianceChart();
        this.createRiskDistributionChart();
        this.createActivityTimelineChart();
        this.createCategoryImpactChart();
    }

    createComplianceChart() {
        const ctx = document.getElementById('complianceChart');
        if (!ctx) return;

        this.charts.compliance = new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: ['Compliant', 'Needs Review', 'Non-Compliant'],
                datasets: [{
                    data: [75, 20, 5],
                    backgroundColor: [
                        '#28a745',
                        '#ffc107',
                        '#dc3545'
                    ],
                    borderWidth: 2,
                    borderColor: '#ffffff'
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: {
                            padding: 20,
                            usePointStyle: true
                        }
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                return `${context.label}: ${context.parsed}%`;
                            }
                        }
                    }
                }
            }
        });
    }

    createRiskDistributionChart() {
        const ctx = document.getElementById('riskChart');
        if (!ctx) return;

        this.charts.risk = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Low', 'Medium', 'High', 'Critical'],
                datasets: [{
                    label: 'Risk Distribution',
                    data: [45, 30, 15, 10],
                    backgroundColor: [
                        '#28a745',
                        '#ffc107',
                        '#fd7e14',
                        '#dc3545'
                    ],
                    borderWidth: 1,
                    borderColor: '#ffffff'
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: {
                            stepSize: 10
                        }
                    }
                },
                plugins: {
                    legend: {
                        display: false
                    }
                }
            }
        });
    }

    createActivityTimelineChart() {
        const ctx = document.getElementById('activityChart');
        if (!ctx) return;

        // Generate sample data for the last 7 days
        const labels = [];
        const data = [];
        for (let i = 6; i >= 0; i--) {
            const date = new Date();
            date.setDate(date.getDate() - i);
            labels.push(date.toLocaleDateString('en-US', { month: 'short', day: 'numeric' }));
            data.push(Math.floor(Math.random() * 20) + 5); // Random activity count
        }

        this.charts.activity = new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Documents Processed',
                    data: data,
                    borderColor: '#007bff',
                    backgroundColor: 'rgba(0, 123, 255, 0.1)',
                    borderWidth: 2,
                    fill: true,
                    tension: 0.4
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: {
                        beginAtZero: true,
                        ticks: {
                            stepSize: 5
                        }
                    }
                },
                plugins: {
                    legend: {
                        display: false
                    }
                }
            }
        });
    }

    createCategoryImpactChart() {
        const ctx = document.getElementById('categoryChart');
        if (!ctx) return;

        this.charts.category = new Chart(ctx, {
            type: 'horizontalBar',
            data: {
                labels: [
                    'Data & Privacy',
                    'Consumer Protection',
                    'Financial Services',
                    'Employment Law',
                    'Intellectual Property',
                    'Environmental',
                    'Healthcare',
                    'Technology'
                ],
                datasets: [{
                    label: 'Impact Level',
                    data: [85, 70, 60, 45, 40, 35, 30, 25],
                    backgroundColor: [
                        '#dc3545',
                        '#fd7e14',
                        '#ffc107',
                        '#28a745',
                        '#20c997',
                        '#17a2b8',
                        '#6f42c1',
                        '#e83e8c'
                    ],
                    borderWidth: 1,
                    borderColor: '#ffffff'
                }]
            },
            options: {
                indexAxis: 'y',
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: {
                        beginAtZero: true,
                        max: 100
                    }
                },
                plugins: {
                    legend: {
                        display: false
                    }
                }
            }
        });
    }

    updateChart(chartName, newData) {
        if (this.charts[chartName]) {
            this.charts[chartName].data = newData;
            this.charts[chartName].update();
        }
    }

    updateComplianceData(compliant, needsReview, nonCompliant) {
        this.updateChart('compliance', {
            labels: ['Compliant', 'Needs Review', 'Non-Compliant'],
            datasets: [{
                data: [compliant, needsReview, nonCompliant],
                backgroundColor: ['#28a745', '#ffc107', '#dc3545'],
                borderWidth: 2,
                borderColor: '#ffffff'
            }]
        });
    }

    updateRiskData(low, medium, high, critical) {
        this.updateChart('risk', {
            labels: ['Low', 'Medium', 'High', 'Critical'],
            datasets: [{
                label: 'Risk Distribution',
                data: [low, medium, high, critical],
                backgroundColor: ['#28a745', '#ffc107', '#fd7e14', '#dc3545'],
                borderWidth: 1,
                borderColor: '#ffffff'
            }]
        });
    }

    updateActivityData(activityData) {
        // activityData should be an array of {date, count} objects
        const labels = activityData.map(item => item.date);
        const data = activityData.map(item => item.count);

        this.updateChart('activity', {
            labels: labels,
            datasets: [{
                label: 'Documents Processed',
                data: data,
                borderColor: '#007bff',
                backgroundColor: 'rgba(0, 123, 255, 0.1)',
                borderWidth: 2,
                fill: true,
                tension: 0.4
            }]
        });
    }

    updateCategoryData(categoryData) {
        // categoryData should be an array of {category, impact} objects
        const labels = categoryData.map(item => item.category);
        const data = categoryData.map(item => item.impact);

        this.updateChart('category', {
            labels: labels,
            datasets: [{
                label: 'Impact Level',
                data: data,
                backgroundColor: this.generateColors(labels.length),
                borderWidth: 1,
                borderColor: '#ffffff'
            }]
        });
    }

    generateColors(count) {
        const colors = [
            '#dc3545', '#fd7e14', '#ffc107', '#28a745',
            '#20c997', '#17a2b8', '#6f42c1', '#e83e8c',
            '#6c757d', '#007bff', '#6610f2', '#6f42c1'
        ];

        const result = [];
        for (let i = 0; i < count; i++) {
            result.push(colors[i % colors.length]);
        }
        return result;
    }

    destroy() {
        Object.values(this.charts).forEach(chart => {
            if (chart) {
                chart.destroy();
            }
        });
        this.charts = {};
    }
}

// Initialize charts when page loads
let legalCharts;
document.addEventListener('DOMContentLoaded', () => {
    legalCharts = new LegalMonitorCharts();
});