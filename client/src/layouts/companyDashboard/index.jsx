import React from 'react';
import { useParams } from 'react-router-dom';
import MinStatCard from '@layouts/companyDashboard/MinStatCard';
import MinStatCard2 from '@layouts/companyDashboard/MinStatCard2';
import '@layouts/companyDashboard/index.scss';
import ChartWrapper from '@layouts/charts/ChartWrapper';
import { CHART_TYPES } from '@constants/variations';

const DUMMY_MINISTAT_DATA = [
  { label: 'Total Active Users', value: '18,765', delta: '2.6', graphType: 'line', graphData: [] },
  { label: 'New Accounts', value: '18,765', delta: '-0.6', graphType: 'line', graphData: [] },
  {
    label: 'Customer Acquisition Cost',
    value: '18,765',
    delta: '2.6',
    graphType: 'bar',
    graphData: [],
  },
  { label: 'Lifetime Value', value: '18,765', delta: '-2.6', graphType: 'bar', graphData: [] },
  { label: 'CAC Payback', value: '18,765', delta: '2.6', graphType: 'line', graphData: [] },
];

const DUMMY_MINISTAT_DATA2 = [
  {
    label: 'Qualified Leads',
    value: '18,765',
    delta: '2.6',
    graphType: 'line',
    graphData: [],
    bgcolor: '#00FF85',
    color: '#005249',
  },
  {
    label: 'Sales Cycle',
    value: '18,765',
    delta: '-0.6',
    graphType: 'line',
    graphData: [],
    bgcolor: '#C8FACD',
    color: '#005249',
  },
  {
    label: 'Average Revenue',
    value: '18,765',
    delta: '2.6',
    graphType: 'line',
    graphData: [],
    bgcolor: '#FFF7CD',
    color: '#7A4F01',
  },
  // Add distribution of accounts pie chart
  {
    label: 'Distribution of accounts',
    // value: '18,765',
    // delta: '-2.6',
    graphType: 'pie',
    graphData: [
      { name: 'Group A', value: 400 },
      { name: 'Group B', value: 300 },
      { name: 'Group C', value: 300 },
      { name: 'Group D', value: 200 },
    ],
  },
  // { label: 'CAC Payback', value: '18,765', delta: '2.6', graphType: 'line', graphData: [] },
];

const CompanyDashboard = () => {
  const { companyName } = useParams();
  return (
    <div className="CompanyDashboard px-10 pb-11">
      <div className="mb-4 flex justify-between">
        <h1 className="font-bold text-3xl text-gray-700">{companyName}</h1>
      </div>
      <div className="flex -mx-10 px-10 hide-scrollbar flex-nowrap overflow-x-auto">
        {DUMMY_MINISTAT_DATA.map((stat) => (
          <MinStatCard {...stat} key={stat.label} />
        ))}
      </div>
      <div className="Row2 flex flex-row justify-evenly hide-scrollbar flex-nowrap">
        <div className="Col1">
          {DUMMY_MINISTAT_DATA2.map((stat) => (
            <MinStatCard2 {...stat} key={stat.label} />
          ))}
        </div>
        <div className="Col2">
          <div className="flex flex-col gap-8">
            <ChartWrapper chartLabel="Active Users Stats" type={CHART_TYPES.LINE} />
            <ChartWrapper chartLabel="Quarterly Recurring Revenue" type={CHART_TYPES.BAR_HZ} />
            <ChartWrapper chartLabel="ARR Growth Rate" type={CHART_TYPES.BAR} />
          </div>
        </div>
        <div className="Col3">
          {DUMMY_MINISTAT_DATA2.map((stat) => (
            <MinStatCard2 {...stat} key={stat.label} />
          ))}
        </div>
      </div>
    </div>
  );
};

export default CompanyDashboard;